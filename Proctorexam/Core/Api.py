import json
import requests

from datetime import datetime

class Api():
    def __init__(self, session, domain, verify=True):
        self.session = session
        self.domain = domain
        self.prefix = "/api/v3/"
        if verify:
            self.url_template = "https://{}.proctorexam.com{}{}"
        else:
            self.url_template = "https://{}.proctorexam.com:3001{}{}"
        self.header = {
            "Accept": "application/vnd.procwise.v3",
            "Authorization": "Token token={}".format(self.session.get_key()),
            "Content-Type": "application/json"
        }
        self.verify = verify

    def clean_path(self, path):
        if path[0] is "/":
            path = path[1:]
        if path[-1] is not "/":
            path = path + "/"

        return path

    def prepare_request(self, path, param):
        url = self.url_template.format(self.domain, self.prefix, path)

        param["nonce"] = str(int(datetime.timestamp(datetime.now()) * 1000))
        param["timestamp"] = str(int(datetime.timestamp(datetime.now()) * 1000))

        base_string, signature = self.session.create_signature(param)
        return url, base_string, signature, param


    def __get(self, path, param):
        url, base_string, signature, __ = self.prepare_request(path, param)
        full_url = url + "?" + base_string.replace("?", "&")

        response = requests.get(full_url+"&signature="+signature, headers=self.header, verify=self.verify)
        return response.content

    def __post(self, path, param):
        url, base_string, signature, params = self.prepare_request(path, param)
        params["signature"] = signature

        response = requests.post(url, json=params, headers=self.header, verify=self.verify)
        return response.content

    def __patch(self, path, param):
        url, base_string, signature, params = self.prepare_request(path, param)
        params["signature"] = signature

        response = requests.patch(url, json=params, headers=self.header, verify=self.verify)
        return response.content

    def __delete(self, path, param):
        url, base_string, signature, params = self.prepare_request(path, param)
        params["signature"] = signature

        response = requests.delete(url, json=params, headers=self.header, verify=self.verify)
        return response.content

    def __put(self, param):
        url, base_string, signature, params = self.prepare_request(path, param)
        params["signature"] = signature

        response = requests.put(url, json=params, headers=self.header, verify=self.verify)
        return response.content

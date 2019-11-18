import json
import requests

from datetime import datetime

class Api():
    def __init__(self, session, domain):
        self.session = session
        self.domain = domain
        self.prefix = "/api/v3/"
        self.url_template = "https://{}.proctorexam.com{}{}"
        self.header = {
            "Accept": "application/vnd.procwise.v3",
            "Authorization": "Token token={}".format(self.session.get_key()),
            "Content-Type": "application/json"
        }

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

        return url, self.session.create_signature(param)


    def __get(self, path, param):
        _, base_string, signature, __ = self.prepare_request(path, param)

        full_url = url + "?" + base_string.replace("?", "&")
        response = requests.get(full_url+"&signature="+signature, headers=self.header)
        return response.content

    def __post(self, path, param):
        url, base_string, signature, params = self.prepare_request(path, param)

        #TODO: check syntax
        response = requests.post(url, params=params, headers=self.header)

    def patch(self, param):
        pass

    def put(self, param):
        pass

    def request(self, param):
        pass

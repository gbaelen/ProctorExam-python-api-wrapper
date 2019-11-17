import json
import requests

from datetime import datetime

class Api():
    def __init__(self, session, domain):
        self.session = session
        self.domain = domain
        self.prefix = "/api/v3"
        self.header = {
            "Accept": "application/vnd.procwise.v3",
            "Authorization": "Token token={}".format(self.session.get_key()),
            "Content-Type": "application/json"
        }

    def get(self, path, param):
        url = "https://{}.proctorexam.com{}{}".format(self.domain, self.prefix, path)
        param["nonce"] = str(int(datetime.timestamp(datetime.now()) * 1000))
        param["timestamp"] = str(int(datetime.timestamp(datetime.now()) * 1000))

        base_string, signature = self.session.create_signature(param)
        
        full_url = url + "?" + base_string.replace("?", "&")
        response = requests.get(full_url+"&signature="+signature, headers=self.header)
        print(response.content)

    def post(self, param):
        pass

    def patch(self, param):
        pass

    def put(self, param):
        pass

    def request(self, param):
        pass

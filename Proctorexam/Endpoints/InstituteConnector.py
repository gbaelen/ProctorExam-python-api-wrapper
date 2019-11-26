import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.Institute import InstituteList, Institute

class InstituteConnector(Api):
    def __init__(self, session, domain, verify):
        Api.__init__(self, session, domain, verify)
        self.session = session
        self.domain = domain

    def get(self, param={}):
        path = "institutes/"

        response = self._Api__get(path, param)
        return response

    def get_institute(self, id, param={}):
        path = f"institutes/{id}"

        if "id" not in param:
            param["id"] = id

        response = self._Api__get(path, param)
        return response

    def create_institute(self, param={}):
        path = "institutes/"

        if "name" not in param:
            raise Exception("Institute name is a required parameter but not found")
        if "short_name" not in param:
            raise Exception("Institute short_name is a required parameter but not found")

        response = self._Api__post(path, param)
        return response

    def update_institute(self, id, param):
        path = f"institutes/{id}"

        if "id" not in param:
            param["id"] = id

        response = self._Api__patch(path, param)
        return response

    def delete_institute(self, id):
        path = f"institutes/{id}"
        param = {"id": id}

        response = self._Api__delete(path, param)
        return response

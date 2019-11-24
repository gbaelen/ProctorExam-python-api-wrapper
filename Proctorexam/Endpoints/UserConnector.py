import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.User import User

class UserConnector(Api):
    def __init__(self, session, domain, verify):
        Api.__init__(self, session, domain, verify)
        self.session = session
        self.domain = domain

    def process(self, response):
        return response

    def create_users_list(self, response_json):
        user_list = UserList()
        for user_json in response_json["users"]:
            user = User.generate_user_from_response(user_json, connector=self)
            user_list.add(user)

        return user_list

    def get_all_users(self, institute_id):
        path = f"institutes/{institute_id}/users"
        param = {"institute_id": institute_id}

        response = self._Api__get(path, param)
        return self.process(response)

    def get_user(self, institute_id, user_id):
        path = f"institutes/{institute_id}/users/{user_id}"
        param = {"id": user_id, "institute_id": institute_id}

        response = self._Api__get(path, param)
        return self.process(response)

    def create_user(self, institute_id, name, email, password, password_confirmation, role):
        path = f"institutes/{institute_id}/users"
        param = {
                    "institute_id": institute_id,
                    "name": name,
                    "email": email,
                    "password": password,
                    "password_confirmation": password_confirmation,
                    "role": role
                }

        response = self._Api__post(path, param)
        return self.process(response)

    def update_user(self, institute_id, user_id, param={}):
        path = f"institutes/{institute_id}/users/{user_id}"

        if "id" not in param:
            param["id"] = id
        if "institute_id" not in param:
            param["institute_id"] = institute_id

        response = self._Api_patch(path, param)
        return self.process(response)

    def delete_user(self, institute_id, user_id):
        path = f"institutes/{institute_id}/users/{user_id}"
        param = {"institute_id": institute_id, "id": user_id}

        response = self._Api__delete(path, param)
        return self.process(response)

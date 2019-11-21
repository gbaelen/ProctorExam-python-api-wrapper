import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.Student import StudentList, Student

class StudentConnector(Api):
    def __init__(self, session, domain):
        Api.__init__(self, session, domain)
        self.session = session
        self.domain = domain

    def check_default_path(self, path):
        if path is None:
            path="student_sessions/"
        else:
            path = self.clean_path(path)
        return path

    def process_patch_response(self, path, response):
        print(response)

    def process_get_response(self, path, response):
        if path == "student_sessions/":
            return self.create_student_list(json.loads(response))
        else:
            print("error")

    def create_student_list(self, response_json):
        student_list = StudentList()
        for student_json in response_json["students"]:
            print(student_json)
            student = Student.generate_student_from_response(student_json, connector=self)
            student_list.add(student)

        return student_list

    def get(self, path=None, param={}):
        path = self.check_default_path(path)

        response = self._Api__get(path, param)
        return self.process_get_response(path, response)

    def patch(self, id, param={}):
        path = "student_sessions/" + id

        response = self._Api__patch(path, param)
        return self.process_patch_response(path, response)

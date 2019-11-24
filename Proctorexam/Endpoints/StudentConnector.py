import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.Student import StudentList, Student

class StudentConnector(Api):
    def __init__(self, session, domain, verify=True):
        Api.__init__(self, session, domain, verify)
        self.session = session
        self.domain = domain

    def check_default_path(self, path):
        if path is None:
            path="student_sessions/"
        else:
            path = self.clean_path(path)
        return path

    def process_post_response(self, path, response):
        print(response)

    def process_patch_response(self, path, response):
        print(response)

    def process_delete_response(self, response):
        print(response)

    def process_get_response(self, path, response):
        if path == "student_sessions/":
            return self.create_student_list(json.loads(response))
        else:
            print("error")
            print(response)

    def create_student_list(self, response_json):
        student_list = StudentList()
        print(response_json)
        for student_json in response_json["students"]:
            print(student_json)
            student = Student.generate_student_from_response(student_json, connector=self)
            student_list.add(student)

        return student_list

    def get(self, path=None, param={}):
        path = self.check_default_path(path)

        response = self._Api__get(path, param)
        return self.process_get_response(path, response)

    def get_by(self, id, path=None, param={}):
        path = f"student_sessions/{id}"
        if "id" not in param:
            param["id"] = id

        response = self._Api__get(path, param)
        return self.process_get_response(path, response)

    def add_to_exam(self, exam_id, params={}):
        path = f"exams/{exam_id}/student_sessions"

        if "id" not in param:
            param["id"] = exam_id

        response = self._Api__post(path, param)
        return self.process_post_response(path, response)

    def edit_student(self, id, param={}):
        path = f"student_sessions/{id}"

        if "id" not in param:
            param["id"] = id

        response = self._Api__patch(path, param)
        return self.process_patch_response(path, response)

    def delete(self, id):
        path = f"student_sessions/{id}"

        response = self._Api__delete(path, {"id": id})
        return self.process_delete_response(response)

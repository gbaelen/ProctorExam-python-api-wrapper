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

    def create_student_from_response(self, response):
        json_response = json.loads(response.content)
        status_code = response.status_code

        if status_code == 201 or status_code == 200:
            return Student.generate_student_from_response(json_response["student"], connector=self)
        elif status_code == 401 or status_code == 403:
            raise UnauthorizedError("User unauthorized", json_response)
        elif status_code == 404:
            raise NotFoundError("Student not found", json_response)
        elif status_code == 422:
            raise BadParametersError("Bad parameters sent", json_response)

    def process_patch_response(self, path, response):
        print(response)

    def process_delete_response(self, response):
        print(response)

    def process_get_response(self, path, response):
        if path == "student_sessions/":
            return self.create_student_list(json.loads(response.content))
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

    def get_student(self, id, path=None, param={}):
        path = f"student_sessions/{id}"
        if "id" not in param:
            param["id"] = id

        response = self._Api__get(path, param)
        return self.create_student_from_response(response)

    def add_to_exam(self, exam_id, param={}):
        path = f"exams/{exam_id}/student_sessions"

        if "exam_id" not in param:
            param["exam_id"] = exam_id

        response = self._Api__post(path, param)
        return self.create_student_from_response(response)

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

# Errors
class BadParametersError(Exception):
    def __init__(self, message, errors):
        super(BadParametersError, self).__init__(message)
        self.errors = errors

class UnauthorizedError(Exception):
    def __init__(self, message, errors):
        super(UnauthorizedError, self).__init__(message)
        self.errors = errors

class NotFoundError(Exception):
    def __init__(self, message, errors):
        super(NotFoundError, self).__init__(message)
        self.errors = errors

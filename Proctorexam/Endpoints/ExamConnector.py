import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.Exam import ExamList, Exam

class ExamConnector(Api):
    def __init__(self, session, domain, verify):
        Api.__init__(self, session, domain, verify)
        self.session = session
        self.domain = domain

    def create_exam_list(self, response_json):
        exam_list = ExamList()
        for exam_json in response_json["exams"]:
            exam = Exam.generate_exam_from_response(exam_json, connector=self)
            exam_list.add(exam)

        return exam_list

    def check_default_path(self, path):
        if path is None:
            path="exams/"
        else:
            path = self.clean_path(path)

        return path

    def process_get_response(self, path, response):
        if path == "exams/":
            return self.create_exam_list(json.loads(response))
        else:
            print("error")

    def process_post_response(self, path, response):
        return "Not implemented yet!"

    def process_patch_response(self, path, response):
        return "Not implemented yet!"

    def process_put_response(self, response):
        print(response)

    def get(self, path=None, param={}):
        path = self.check_default_path(path)

        response = self._Api__get(path, param)
        return self.process_get_response(path, response)

    def get_exam(self, id, path=None, param={}):
        path = f"student_sessions/{id}"
        if "id" not in param:
            param["id"] = id

        response = self._Api__get(path, param)
        return response

    def get_all_students_in_exam(self, id, param={}):
        path = f"exams/{id}/index_students"

        if "id" not in param:
            param["id"] = id

        response = self._Api__get(path, param)
        return response

    def get_student_in_exam_by_id(self, student_id, exam_id, param={}):
        path = f"exams/{exam_id}/show_student"

        if "id" not in param:
            param["id"] = exam_id
        if "student_session_id" not in param:
            param["student_session_id"] = student_id

        response = self._Api__get(path, param)
        return response

    def get_student_in_exam_by_lti_id(self, student_lms_id, resource_link_id, exam_id):
        path = f"exams/{id}/show_lti_student"
        param = {
            "student_lms_id": lms_id,
            "resource_link_id": resource_link_id,
            "id": id
        }

        response = self._Api__get(path, param)
        return response

    def create_exam(self, path=None, param=None):
        path = "exams/"

        if param is None:
            raise Exception("Params in post cannot be empty!")
        else:
            if param["name"] is None:
                raise Exception("Exam name is a required param but not found")
            if param["type"] is None:
                raise Exception("Exam type is a required param but not found")

        response = self._Api__post(path, param)
        return response

    def register_student_in_exam(self, id, param={}):
        path = f"exams/{id}/add_student"

        if "id" not in param:
            param["id"] = id
        if "name" not in param:
            raise Exception("Student name is a required param but not found")
        if "email" not in param:
            raise Exception("Student email is a required param but not found")

        response = self._Api__post(path, param)
        return response

    def update_exam(self, id, param={}):
        path = f"exams/{id}"

        response = self._Api__patch(path, param)
        return response

    def send_all_exam_emails(self, id):
        path = f"exams/{id}/send_emails"
        param = {"id": id}

        response = self._Api__post(path, param)
        return response

    def add_comanager_in_exam(self, exam_id, user_id):
        path = f"exams/{exam_id}/add_comanager"
        param = {"id": id, "comanager_id": user_id}

        response = self._Api__put(path, param)
        return response

    def delete_exam(self, id):
        path = f"exams/{id}"

        response = self._Api__delete(path, {"id": id})
        return response

    def delete_comanager(self, exam_id, user_id):
        path = f"exams/{id}/remove_comanager"
        param = {"id": id, "comanager_id": user_id}

        response = self._Api__delete(path, param)
        return response

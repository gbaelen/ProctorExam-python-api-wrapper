import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.Exam import ExamList, Exam

class ExamConnector(Api):
    def __init__(self, session, domain):
        Api.__init__(self, session, domain)
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

    def get(self, path=None, param={}):
        path = self.check_default_path(path)

        response = self._Api__get(path, param)
        return self.process_get_response(path, response)

    def get_all_students_in_exam(self, id):
        path = "exams/{}/index_students".format(id)

        response = self._Api__get(path, {"id":id})
        return response

    def post(self, path=None, param=None):
        path = self.check_default_path(path)

        if param is None:
            raise Exception("Params in post cannot be empty!")
        else:
            if param["name"] is None:
                raise Exception("Exam name is a required param but not found")
            if param["type"] is None:
                raise Exception("Exam type is a required param but not found")

        response = self._Api__post(path, param)
        return self.process_post_response(path, response)

    def patch(self, id, param={}):
        path = "exams/" + id

        response = self._Api__patch(path, param)
        return self.process_patch_response(path, response)

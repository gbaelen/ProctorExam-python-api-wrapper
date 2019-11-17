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
            exam = Exam.generate_exam_from_response(exam_json)
            exam_list.add(exam)

        return exam_list

    def process_get_response(self, path, response):
        if path == "exams/":
            return self.create_exam_list(json.loads(response))
        else:
            print("error")

    def get(self, path=None, param=None):
        if path is None:
            path="exams/"
        else:
            path = self.clean_path(path)

        if param is None:
            param={}

        response = self._Api__get(path, param)
        return self.process_get_response(path, response)

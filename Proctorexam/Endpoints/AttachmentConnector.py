import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.Attachment import AttachmentList, Attachment

class AttachmentConnector(Api):
    def __init__(self, session, domain, verify):
        Api.__init__(self, session, domain, verify)
        self.session = session
        self.domain = domain

    def get(self, exam_id, param={}):
        path = f"exams/{exam_id}/attachments"

        if "exam_id" not in param:
            param["exam_id"] = exam_id

        response = self._Api__get(path, param)
        return response

    def get_attachment_in_exam(self, exam_id, attachment_id, param={}):
        path = f"exams/{exam_id}/attachments/{attachment_id}"

        if "exam_id" not in param:
            param["exam_id"] = exam_id
        if "id" not in param:
            param["id"] = attachment_id

        response = self._Api__get(path, param)
        return response

    def delete_attachment(self, exam_id, attachment_id):
        path = f"exams/{exam_id}/attachments/{attachment_id}"
        param = {"id": attachment_id, "exam_id": exam_id}

        response = self._Api__delete(path, param)
        return response

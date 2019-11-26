import json

from Proctorexam.Core.Api import Api
from Proctorexam.Classes.Document import DocumentList, Document

class DocumentConnector(Api):
    def __init__(self, session, domain, verify):
        Api.__init__(self, session, domain, verify)
        self.session = session
        self.domain = domain

    def get(self, exam_id, param={}):
        path = f"exams/{exam_id}/documents"

        if "exam_id" not in param:
            param["exam_id"] = exam_id

        response = self._Api__get(path, param)
        return response

    def get_document_in_exam(self, exam_id, document_id, param={}):
        path = f"/exams/{exam_id}/documents/{document_id}"

        if "exam_id" not in param:
            param["exam_id"] = exam_id
        if "id" not in param:
            param["id"] = document_id

        response = self._Api__get(path, param)
        return response

    def create_document(self, exam_id, param={}):
        path = f"exams/{exam_id}/documents"

        if "exam_id" not in param:
            param["exam_id"] = exam_id
        if "exam_content" not in param:
            raise Exception("Document exam_content is a required parameter but was not found.")

        response = self._Api__post(path, param)
        return response

    def update_document(self, exam_id, document_id, param={}):
        path = f"exams/{exam_id}/documents/{document_id}"

        if "exam_id" not in param:
            param["exam_id"] = exam_id
        if "id" not in param:
            param["id"] = document_id
        if "exam_content" not in param:
            raise Exception("Document exam_content is a required parameter but was not found.")

        response = self._Api__patch(path, param)
        return response

    def delete_document(self, exam_id, document_id):
        path = f"exams/{exam_id}/documents/{document_id}"
        param = {"id": document_id, "exam_id": exam_id}

        response = self._Api__delete(path, param)
        return response

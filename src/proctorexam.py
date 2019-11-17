import sys
import os

sys.path.append( os.path.join( os.path.dirname(__file__), '..' ) )

from src.Core.Session import Session
from src.Endpoints.ExamConnector import ExamConnector
from src.Endpoints.StudentConnector import StudentConnector

class Proctorexam():
    """
    """
    def __init__(self, domain, key=None, secret=None, region=None):
        self.session = Session.create_credentials(key, secret)
        self.exam = ExamConnector(self.session, self.clean_domain(domain))
        self.student = StudentConnector(self.session, self.clean_domain(domain))

    def clean_domain(self, domain):
        return domain.replace("https://", "").replace("http://", "").replace(".proctorexam.com", "")

if __name__ == "__main__":
    proctorexam = Proctorexam("webrtc")
    #print(proctorexam.exam.get("/exams/8", {"id": "8"}))
    exams = proctorexam.exam.get()

    for exam in exams:
        if exam.id == 766:
            print(exam.name)
            print(exam.get_exam_type())

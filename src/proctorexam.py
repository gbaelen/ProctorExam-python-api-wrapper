import sys
import os

sys.path.append( os.path.join( os.path.dirname(__file__), '..' ) )

from src.core.Session import Session
from src.exam.Exam import Exam

class Proctorexam():
    """
    """
    def __init__(self, domain, key=None, secret=None, region=None):
        self.session = Session.create_credentials(key, secret)
        self.exam = Exam(self.session, self.clean_domain(domain))

    def clean_domain(self, domain):
        return domain.replace("https://", "").replace("http://", "").replace(".proctorexam.com", "")

if __name__ == "__main__":
    proctorexam = Proctorexam("")
    print(proctorexam.exam.get("/exams/8", {"id": "8"}))

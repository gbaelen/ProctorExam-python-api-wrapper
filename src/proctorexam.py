import sys
import os

sys.path.append( os.path.join( os.path.dirname(__file__), '..' ) )

from src.exam.Exam import Exam

class Proctorexam():
    """
    """
    def __init__(self):
        self.exam = Exam

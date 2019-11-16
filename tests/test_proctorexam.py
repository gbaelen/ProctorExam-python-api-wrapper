import sys
import os

sys.path.append( os.path.join( os.path.dirname(__file__), '..' ) )

from src.Proctorexam import Proctorexam

def test_proctorexam_exam():
    """ Tests an API call to get an exam informations """
    proctorexam = Proctorexam()
    response = proctorexam.exam.get(1)

    assert isinstance(response, dict)
    assert response['id'] == 1

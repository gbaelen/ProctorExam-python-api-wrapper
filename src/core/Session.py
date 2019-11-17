import os
import sys
import json
from collections import namedtuple

sys.path.append( os.path.join( os.path.dirname(__file__), '..' ) )

from src.Core import Signer

Credentials = namedtuple('Credentials', 'key secret')

def check_environment_variables():
    key = os.environ.get('PROCTOREXAM_API_KEY')
    secret = os.environ.get('PROCTOREXAM_API_SECRET')
    if key is not None and secret is not None:
        return (key, secret)
    else:
        return False

class Session():
    def __init__(self):
        self.__credentials = None
        self.signature = None

    @staticmethod
    def create_credentials(key, secret):
        if key is None and secret is None:
            environment_variables = check_environment_variables()
            if environment_variables:
                key = os.environ.get('PROCTOREXAM_API_KEY')
                secret = os.environ.get('PROCTOREXAM_API_SECRET')
            else:
                raise Exception('KEY and SECRET not found. Please add the environment variables "PROCTOREXAM_API_KEY" and "PROCTOREXAM_API_SECRET"')

        session = Session()
        session.set_credentials(Credentials(key, secret))
        return session

    def create_signature(self, param):
        return Signer.create_signature(param, self.__credentials.secret)

    def set_credentials(self, credentials):
        self.__credentials = credentials

    def get_key(self):
        return self.__credentials.key

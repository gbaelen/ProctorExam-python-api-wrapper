from src.Core.Api import Api

class Exam(Api):
    def __init__(self, session, domain):
        Api.__init__(self, session, domain)
        self.session = session
        self.domain = domain

    def get(self, path=None, param=None):
        if path is None:
            path="exams/"
        else:
            path = self.clean_path(path)

        if param is None:
            param={}

        self._Api__get(path, param)

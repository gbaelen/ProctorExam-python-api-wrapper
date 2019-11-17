from src.core.Api import Api

class Exam(Api):
    def __init__(self, session, domain):
        Api.__init__(self, session, domain)
        self.session = session
        self.domain = domain

from src.Core.Api import Api

class Student(Api):
    def __init__(self, session, domain):
        Api.__init__(self, session, domain)
        self.session = session
        self.domain = domain

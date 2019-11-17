from Proctorexam.Core.Api import Api

class StudentConnector(Api):
    def __init__(self, session, domain):
        Api.__init__(self, session, domain)
        self.session = session
        self.domain = domain

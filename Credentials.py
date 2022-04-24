class Credential:
    credentsList = []

    def __init__(self, applicationName, username, password):
        self.applicationName = applicationName
        self.username = username
        self.password = password

    def saveCredential(self):
        Credential.credentsList.append(self)


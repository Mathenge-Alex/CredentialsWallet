class Credential:
    credentialsList = []

    def __init__(self, applicationName, accountName, passKey):
        self.applicationName = applicationName
        self.accountName = accountName
        self.passKey = passKey

    def save_credentials(self):
        Credential.credentsList.append(self)

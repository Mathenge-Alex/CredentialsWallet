class Credential:
    vault = []

    def __init__(self, applicationName, accountName, passKey):
        self.applicationName = applicationName
        self.accountName = accountName
        self.passKey = passKey

    def save_credentials(self):
        Credential.vault.append(self)

    @classmethod
    def search_name(cls, appName):
        for Credent in cls.vault:
            if Credent.applicationName == appName:
                return Credential

    @classmethod
    def show_credentials(cls):
        return cls.vault


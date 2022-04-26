class Credential:
    vault = []

    def __init__(self, applicationName, accountName, passKey):
        self.applicationName = applicationName
        self.accountName = accountName
        self.passKey = passKey

    def save_credentials(self):
        Credential.vault.append(self)

    def delete_credential(self, appName):
        Credential.vault.pop(appName)

    @classmethod
    def search_name(cls, applicationName):
        for Credent in cls.vault:
            if Credent.applicationName == applicationName:
                return Credential

    @classmethod
    def show_credentials(cls):
        return cls.vault

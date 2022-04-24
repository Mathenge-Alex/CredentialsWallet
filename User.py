from typing import Dict, Any


class CAUser:
    user_account = []

    def __int__(self, username, password):
        self.username = username
        self.password = password

    def save_account(self):
        CAUser.user_account.append(self)

    def delete_account(self):
        CAUser.user_account.remove(self)

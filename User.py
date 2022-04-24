from typing import Dict, Any


class User:
    user_accounts: Dict[Any, Any] = {}

    def __int__(self, username, password):
        self.username = username
        self.password = password

    def create_account(self):
        User.user_accounts.update(self)

    def delete_account(self):
        User.user_accounts.pop(self)

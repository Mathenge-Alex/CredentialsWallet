import unittest

import User
from Credentials import Credential

class runTests(unittest.TestCase):
    def setUp(self) -> None:
        self.new_account = Credential("arx", "mna")

    def init_test(self):
        self.assertEqual(self.new_account.accountName, "arx")
        self.assertEqual(self.new_account.passKey, "mna")

    def save_user_test(self):
        self.new_account.save_credentials()
        self.assertEqual(len(User.CAUser),1)
    def find_user_test(self):
        self.new_account.save_credentials()
        test_user = Credential("arx", "mna")
        test_user.save_credentials()
        search_user = Credential.search_name("arx")
        self.assertEqual(search_user.passkey, test_user.passKey )
    def show_user_test(self):
        self.assertEqual((Credential.show_credentials(), Credential.vault))
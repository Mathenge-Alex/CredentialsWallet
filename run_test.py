import unittest
from unittest import result

import User
from Credentials import Credential


class runTests(unittest.TestCase):
    def test_setUp(self) -> None:
        self.new_account = Credential("arx", "mna", "A1234")
        # self.assertEqual(result, "arx", "mna", "A1234")

    def init_test(self):
        '''
        Object initialization test. Checks whether it it properly done
        '''
        self.assertEqual(self.new_account.accountName, "arx")
        self.assertEqual(self.new_account.passKey, "mna")

    def save_user_test(self):
        '''
        Checking whether the new user profile is created saved successfully
        '''
        self.new_account.save_credentials()
        self.assertEqual(len(User.save_account()), 1)

    def find_user_test(self):
        self.new_account.save_credentials()
        test_user = Credential("arx", "mna")
        test_user.save_credentials()
        search_user = Credential.search_name("arx")
        self.assertEqual(search_user.passkey, test_user.passKey)

    def show_user_test(self):
        self.assertEqual((Credential.show_credentials(), Credential.vault))
    

if __name__ == '__main__':
    unittest.main()
import Credentials
from User import CAUser
from Credentials import Credential


def create_account(username, password):
    new_account = CAUser(username, password)
    return new_account


def save_account(User):
    User.save_account()

def main():
        print(f"\n Use Credential Wallet (CWallet) is a safe vault for all your online passwords. \n"
          f"\n"
          f"\n Create an account With Us to store your passwords.\n \n")
        print("Enter your Preferred CWallet username: ")
        userName = input()
        print("Enter your Preferred CWallet password: ")
        Password = input()
        save_account(create_account(userName, Password))

        print(f"\n Welcome to CWallet. Your account ${userName} has been created. "
              f"\n Please LOGIN to START storing your credentials")
        print("\n Enter Your CWallet Username: ")
        user_name = input()
        print("\n Enter Your CWallet Password: ")
        user_password = input()



if __name__ == '__main__':
    main()


    # save_account()


# menu = ""
# while menu != "1" or menu != "2":





# def new_user(self, username, password):
#     new_account = User.create_account()
#     return new_account
#     print("Credential created successfully")
#     print(new_user_account())

# credential_selected = "Tim"if

#
#
# def delete_credential():
#     print(f'Credential ${credential_selected} deleted')
#
#
# print("NEW CREDENTIAL "
#       "\n -------------- \n "
#       "Account Name is:")

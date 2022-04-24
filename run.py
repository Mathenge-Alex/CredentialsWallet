from User import CAUser
from Credentials import Credential
import random


def create_account(username, password):
    new_account = CAUser()
    return new_account


def save_account(User):
    User.save_account()

    #     Credentials


def create_credential(applicationName, accountName, passKey):
    new_credential = Credential(applicationName, accountName, passKey)
    return new_credential


def save_credential(Credentials):
    Credential.save_credentials()


def find_credential(applicationName):
    return Credential.search_name(applicationName)


def main():
    print(f"\n Use Credential Wallet (CWallet) is a safe vault for all your online passwords. \n"
          f"\n"
          f"\n Create an account With Us to store your passwords.\n \n")
    print("Enter your Preferred CWallet username: ")
    userName = input()
    print("Enter your Preferred CWallet password: ")
    passWord = input()
    save_account(create_account(userName, passWord))

    print(f"\n Welcome to CWallet. Your account {userName} has been created. "
          f"\n Please LOGIN to START storing your credentials")
    print("\n Enter Your CWallet Username: ")
    user_name = input()
    print("\n Enter Your CWallet Password: ")
    user_password = input()

    while True:
        if userName == user_name:
            print(f"welcome {user_name}. Type :=>:\n"
                  f"C : Store New Credentials \n"
                  f"S : Show Existing Credentials \n"
                  f"F : Find a Credential by Application Name"
                  f"D : Delete a credential")
            option = input("Type your Selection here: ")
            if option == 'C':
                print(f"Creating a new Credential\n")
                applicationName = input("Enter the application name: ")
                accountName = input("Enter the application PassKey: ")
                print("Do you want CWallet to generate a passKey for You or Your Own Password?")
                keyOption = input("Y :Generate for me \t N : Own passKey").upper()
                if keyOption == 'Y':
                    salt = str(random.randrange(127, 309))
                    passKey = accountName.join(salt)

                else:
                    passKey = input("Enter Your PassKey: ")

                save_credential(create_credential(applicationName, accountName, passKey))
                print(f"\n{accountName} Credentials Saved successfully")


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

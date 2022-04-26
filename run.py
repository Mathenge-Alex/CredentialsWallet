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


def show_credentials():
    return Credential.show_credentials()


def main():
    # Creating a CWallet Account to Start Saving Credentials.
    print(f"\n Use Credential Wallet (CWallet) is a safe vault for all your online passwords. \n"
          f"\n"
          f"\n Create an account With Us to store your passwords.\n \n")
    userName = input("Enter your Preferred CWallet username: ")
    passWord = input("Enter your Preferred CWallet password: ")
    save_account(create_account(userName, passWord))

    print(f"\n Welcome to CWallet. Your account {userName} has been created. "
          f"\n Please LOGIN to START storing your credentials")
    user_name = input("\n Enter Your CWallet Username: ")
    user_password = input()
    "\n Enter Your CWallet Password: "
    while True:
        # Options to select from
        if userName == user_name:
            print(f"welcome {user_name}. Type :=>:\n"
                  f"C : Store New Credentials \n"
                  f"S : Show Existing Credentials \n"
                  f"F : Find a Credential by Application Name"
                  f"D : Delete a credential")
            option = input("Type your Selection here: ").upper()

            # Create a New credential
            if option == 'C':
                print(f"Creating a new Credential\n")
                applicationName = input("Enter the application name: ")
                accountName = input("Enter User Account Name: ")
                print("Do you want CWallet to generate a passKey for You or Your Own Password?")
                keyOption = input("Y :Generate for me \t N : Own passKey ").upper()
                if keyOption == 'Y':
                    salt = str(random.randrange(127, 309))
                    passKey = accountName.join(salt)

                else:
                    passKey = input("Enter Your PassKey: ")

                save_credential(create_credential(applicationName, accountName, passKey))
                print(f"\n{accountName} Credentials Saved successfully")

            # Find Existing Credentials
            elif option == 'F':
                print(f"Enter the Application Name You Want to Search For: ")
                search = input("Enter the Application's Name: ")
                if find_credential(search):
                    query = find_credential(search)
                    print(f"Here are the results\n"
                          f"Application Name: {query.applicationName}\n"
                          f"Username: {query.accountName}\n"
                          f"Password: {query.passkey}\n")
                else:
                    print(f"The credential {search} does not exist!"
                          f"If You Can't Find the Application Name, Create a New Credential.")

            # show Existing Credentials
            elif option == 'S':
                if show_credentials():
                    print("Here are your existing credentials: \n")
                    for credent in show_credentials():
                        print(f"App Name: {credent.applicationName} \n"
                              f"Account Name: {credent.accountName}  \n"
                              f"Password: {credent.passKey} \n")
                else:
                    print("You do not have saved Credentials. \n"
                          "Select 'C' to store new credentials")

            #         Delete Credential function
            # elif option == 'D':


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

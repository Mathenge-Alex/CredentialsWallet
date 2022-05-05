from User import CAUser
from Credentials import Credential
import random


def create_account(username, password):
    '''
    Function to create a new CWallet Account
    '''
    new_account = CAUser()
    return new_account


def save_account(User):
    '''
    Function to save a new CWallet Account credentials.
    '''
    User.save_account()

    #     Credentials

def create_credential(applicationName, accountName, passKey):
    '''
    creating an app credential (appname, Username, password)
    '''
    new_credential = Credential(applicationName, accountName, passKey)
    return new_credential


def save_credential(credential):
    '''
    Saving the user's credentials.
    '''
    credential.save_credentials()


def find_credential(applicationName):
    '''
    Searching for saved credentials
    '''
    return Credential.search_name(applicationName)


def show_credentials():
    '''
    Displaying saved credentials
    '''
    return Credential.show_credentials()


def delete_credential(credential):
    '''
    Deleting existing credentials from the vault.
    '''
    credential.delete_credential()


def main():
    '''
    Runs the application and allows the user to create a new CWallet account.
    '''
    # Creating a CWallet Account to Start Saving Credentials.
    print(f"\n\n \t \t WELCOME TO CREDENTIALS WALLET"
        f"\n Use Credential Wallet (CWallet) as a safe vault for all your online passwords. \n"
        f"\n Create an account With Us to store your passwords.\n")
    userName = input("Enter your Preferred CWallet username: ")
    passWord = input("Enter your Preferred CWallet password: ")
    save_account(create_account(userName, passWord))

    print(f"\n Welcome to CWallet. Your account {userName} has been created. "
        f"\n Please LOGIN to START storing your credentials")
    user_name = input("\n Enter Your CWallet Username: ")
    user_password = input("Enter Your CWallet Password: ")
    "\n Enter Your CWallet Password: "
    while True:
        # Options to select from
        if userName == user_name:
            '''
                Validates the input username and pasword. Rejects entry if they do not match. On success, the user selects a entry to continue.
            '''
            print(f"welcome {user_name}. Type :=>:\n"
                f"C : Store New Credentials \n"
                f"S : Show Existing Credentials \n"
                f"F : Find a Credential by Application Name\n"
                f"D : Delete a Credential\n"
                f"E : Exit The Cwallet App\n")
            option = input("Type your Selection here: ").upper()

            # Create a New credential
            if option == 'C':
                '''
                Entry to create a new app credential
                '''
                print(f"Creating a new Credential\n")
                applicationName = input("Enter the application name: ")
                accountName = input("Enter User Account Name: ")
                print("Do you want CWallet to generate a passKey for You or Your Own Password?")
                keyOption = input("Y :Generate for me \t N : Own passKey ").upper()

                # Auto-Generated Password
                if keyOption == 'Y':
                    '''
                Entry to receive an auto-generated password for the credential
                '''
                    salt = str(random.randrange(127, 309))
                    passKey = accountName.join(salt)
                    print("Your Password has Been Generated: ")
                    save_credential(create_credential(applicationName, accountName, passKey))

                # Custom Password
                elif keyOption == 'N':
                    '''
                Creating a password by oneself.
                '''
                    passKey = input("Enter Your PassKey: ")
                    save_credential(create_credential(applicationName, accountName, passKey))
                print(f"\n{accountName} Credentials Saved successfully")

            # Find Existing Credentials
            elif option == 'F':
                '''
                Finding an existing credential
                '''
                print(f"Enter the Application Name You Want to Search For: ")
                appName = input("Enter the Application's Name: ")
                if find_credential(appName):
                    query = find_credential(appName)
                    print(f"Here are the results\n"
                        f"Application Name: {query.applicationName}\n"
                        f"Username: {query.accountName}\n"
                        f"Password: {query.passkey}\n")
                else:
                    print(f"The credential {appName} does not exist!"
                        f"If You Can't Find the Application Name, Create a New Credential.")

            # show Existing Credentials
            elif option == 'S':
                '''
                Displaying the found existing credential
                '''
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
            elif option == 'D':
                '''
                Delete a stored credential
                '''
                applicationName = input("Enter the app name of Credential To Delete")
                if find_credential(applicationName):
                    appName = find_credential(applicationName)
                    Credential.delete_credential(appName)
                    print(f"Your {appName} Account has Been deleted successfully")
                else:
                    print(f"The Credential \"{applicationName}\" You want to delete does not exist")

            #         Exit From the CWallet App
            elif option =='E':
                '''
                Exit from the application.
                '''
                print(f"It was great serving you {userName}. Thank you for esteeming CWallet with your passwords. \n \t\t See You Later!")
                break

            # When a wrong Entry is made.
            else:
                print("You have Made an Invalid Entry. Please Try Again")
        else:
            print("Wrong Username or Password. Please Try Again or Create an account if Not Yet")

            """
            
            """


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

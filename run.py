#!/usr/bin/env python3.10.4
from user import User
import getpass
import random
import string
dash = '-' * 60

def create_account(account_name,username,password,confirm_password):

    """
    function to create a new account
    """

    new_user = User(account_name,username,password,confirm_password)

    return new_user

def save_details(user):

    """
    function to save_details
    """
    user.save_detail()

def display_all_details():

    """
    function used to return all saved details
    """
    return User.display_all_details()

def check_existing_user(username):

    """
    function that is used to check and return all existing accounts
    """

    return User.user_exist(username)

def find_user(username):

    """
    function is used check details from save_details
    """

    return User.find_by_username(username)

def generatePassword(num):
   genpas = ''

   for n in range(num):
       x = random.randint(0,94)
       genpas += string.printable[x]

   return genpas

def main():
    print('{:_^5}'.format('WELCOME TO PASSWORD LOCKER!'))


    print('\n')

    print('{:_^20}'.format('login'))

    print('\n')

    print("Please enter your username")

    user_name = input().upper()

    print(f"Hello {user_name}, what do you want to do?")

    print('\n')

    while True:

        list =(''' use the following short codes:
        1-Register a new account
        2-Display accounts
        3-Find accounts
        4-Exit the locker\n''')
        print(list)



        short_code = input().lower()

        if short_code == '1':

            print(f"{user_name} Please fill the following")

            print("-"*10)

            print ("Account name")

            account_name = input()

            print('\n')

            print("Username")
            username = input()

            print('\n')

            print("Do you want a randomly generated password?")


            print("yes", "no")
            ans = input().lower()

            if ans == 'yes':
                length = int(input('\nEnter the length of password:'))
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                num = string.digits
                symbols = string.punctuation

                all = lower + upper + num + symbols
                temp = random.sample(all, length)
                password = " ".join(temp)
                print(password)

                # save_details(create_account(account_name,username,password,confirm_password))
                # print ('\n')
                print(f"{user_name} {account_name} your account {username} is created and password saved")

                print ('\n')
                
            elif ans == 'no':
                password = getpass.getpass('password:')
                print("*********")

                confirm_password = getpass.getpass('confirm password:')
                print("*********")

                save_details(create_account(account_name,username,password,confirm_password))

                print ('\n')

                print(dash)

                print(f"Hey {user_name}")
                print(f"Your account name is {account_name}.com")
                print(f"Your account username is {username}")

                print(dash)

                print ('\n')

                print(f"{user_name} what else do you want to do?")

        elif short_code =='2':


            if display_all_details():

                print(f"{user_name} here is a list of all your saved accounts")

                print('\n')

                for user in display_all_details():

                    print(dash)

                    print(f"Account is {user.account_name}.com")
                    print(f"Account username is {user.username}")
                    print(f"The account's password is {user.password}")

                    print(dash)

                    print('\n')

                    print(f"{user_name} what else do you want to do?")

            else:

                print('\n')

                print(f" {user_name} You dont seem to have any contacts saved yet")

                print('\n')

                print(f"{user_name} what else do you want to do?")

        elif short_code == '3':

            print(f"{user_name} Enter a username you want to search for")

            search_username = input()


            if check_existing_user(search_username):

                search_username = find_user(search_username)

                print(dash)

                print(f"Account is {search_username.account_name}.com")
                print(f"Account username is {search_username.username}")
                print(f"Account password is {search_username.password}")

                print(dash)

                print(f"{user_name} what else do you want to do?")

            else:
                print(f"{user_name} That account does not exist")

                print(f"{user_name} what else do you want to do?")

        elif short_code == "4":

            print("Bye .......")

            break

        else:
            print("I really didn't get that. Please use the correct code")

            print(f"{user_name} what else do you want to do?")


if __name__ == '__main__':

    main()                 
      

  
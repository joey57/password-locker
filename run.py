from getpass import getpass
import random
from user import User
from credential import Credentials
dash = '-'*60

def create_account(account_name, username, password, confirm_password):
  '''
  function to create an account
  '''
  new_user = User(account_name, username, password,confirm_password)
  return new_user

def save_details(user):
  '''
  function to save details
  '''
  user.save_detail()

def display_all_details():
  '''
  function to display the saved details
  '''
  return User.display_all_details()

def check_existing_user(username):
  '''
  function to check and return existing accounts
  '''
  return User.user_exist(username)

def find_user(username):
  '''
  function to check details from save_details
  '''
  return User.user.find_by_username(username)

def main():
  print("Welcome this is password locker!")
  print('\n')
  print("login")
  print("\n")

  print("What is your username?")
  user_name = input()

  print(f"Hello {user_name}, welcome to password locker, what would you like to do")
  print('\n')

  while True:
    print("Use the following short codes: 1- register a new account, 2- display account, 3- find contacts, 4-exit password locker")

    short_code = input().lower()

    if short_code == '1':
      print(f"{user_name} please fill int the following")

      print("First name")
      f_name = input()
      print("-"*10)
      print("account name")
      account_name = input()

      print("username")
      username = input()
      

      print("Do you want a randomly generated password?")
      ans = input()

      password = getpass.getpass('password:')
      print("*****")
      confirm_password = getpass.getpass('confirm password:')
      print("*****")
      save_details(create_account(account_name,password,confirm_password)) 
      print('\n')
      print(f"{user_name} {account_name} account of {username} created and password save")
      print('\n')

      print(f"{user_name} what else do you want to do")

    elif short_code == '2':
      if display_all_details():
        print(f"{user_name} here is a list of all your accounts")
        print('\n')
        for user in display_all_details():
          print(f"{user.account_name} {user.username}.......{user.password}")
          print('\n')
      else:
        print('\n')
        print(f"{user_name} you dont seem to have any account saved yet")
        print('\n')

    elif short_code == '3': 
      print(f"Enter the username you want to search for")
      search_username = input()
      if check_existing_user(search_username):
        search_username = find_user(search_username) 

        print(dash)

        print(f"Account is {search_username.account_name}.com")
        print(f"Account username is {search_username.username}")
        print(f"Account password is {search_username.password} dont give out passwords")

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
          
if __name__ == "__main__":
  main()          
      

  
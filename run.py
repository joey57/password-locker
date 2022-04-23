from getpass import getpass
import random
from user import User
from credential import Credentials

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

def main():
  print("Welcome this is password locker!")
  print('\n')

  print("What is your name?")
  user_name = input()

  print(f"Hello {user_name}, welcome to password locker, what would you like to do")
  print('\n')

  while True:
    print("Use the following short codes: 1- register a new account, 2- display account, 3- find contacts, 4-exit password locker")

    short_code = input().lower()
    if short_code == '1':
      print("Hey new user")
      print("-"*10)
      print("First name")
      f_name = input()
      print("Last name")
      l_name = input()
      print("username")
      print('\n')

      print("Do you want a randomly generated password?")
      ans = input()
      ans = input()
      if ans:
         WORDS = ("{user_name}", "{user_name}123", "{user_name}zyx", "{user_name}098", "{user_name}567",  "{user_name}hfg")
         word = random.choice(WORDS)
         correct = word
         jumble = ""
         while word:
              position = random.randrange(len(word))
              word = word[:position] + word[(position + 1):]
         print(word[position])
      else:
        password = getpass.getpass('password:')
        print("*****")
        confirm_password = getpass.getpass('confirm_password')
        print("*****")

      save_details(create_account(f_name,l_name,password,confirm_password)) 
      print('\n')
      print(f"New user {f_name} {password} account created and password save")
      print('\n')
      
if __name__ == "__main__":
  main()          
      

  
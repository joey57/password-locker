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


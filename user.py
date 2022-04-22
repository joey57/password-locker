class User:
  '''
  Class that generates new instances of users
  '''
  user_detail = []
  
  def __init__(self, login_account, login_username):
    '''
    _inti_ method that helps us define properties for our objects
    '''
    self.login_username = login_username
    self.login_account = login_account

    
        
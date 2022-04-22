class User:
  '''
  Class that generates new instances of users
  '''
  # empty list where user accounts will be created
  accounts_list = []
  
  def __init__(self, username, account):
    '''
    _inti_ method that helps us define properties for our objects
    '''
    self.username = username
    self.account = account

    
        
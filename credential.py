class Credentials:
  '''
  Class that generates new instances of passwords
  '''
  credentials_list= []

  def __init__(self, login_credentials):
    '''
    __init__ method that helps us define properties for our objects
    '''
    self.login_credentials = login_credentials

      
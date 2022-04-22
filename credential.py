class Credential:
  '''
  Class that generates new instances of passwords
  '''
  credentials_list= []

  def __init__(self, login_credential):
    '''
    __init__ method that helps us define properties for our objects
    '''
    self.login_credential = login_credential

      
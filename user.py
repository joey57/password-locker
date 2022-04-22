class User:
  '''
  Class that generates new instances of users
  '''
  # empty list where user accounts will be created
  user_detail = []
  
  def save_detail(self):
    '''
    save-detail method saves user object into user-detail list
    '''
    User.user_detail.append(self)
  
  def __init__(self, account_name, username, password):
    '''
    _inti_ method that helps us define properties for our objects
    '''
    self.account_name = account_name
    self.username = username
    self.password = password
    

  def delete_detail(self):
    '''
    delete_detail method deletes a saved user detail from user detail list
    '''  
    User.user_detail.remove(self)

  @classmethod
  def display_all_details(cls):
    '''
    method that return the user detail list
    '''  
    return cls.user_detail

    
        
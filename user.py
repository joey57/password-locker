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
  
  def __init__(self, first_name, last_name, username, password, confirm_password):
    '''
    _inti_ method that helps us define properties for our objects
    '''
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.password = password
    self.confirm_password = confirm_password
    

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

  @classmethod
  def find_by_username(cls, username):
    '''
    method that takes in an account and returns an account that matches
    '''  
    for user in cls.user_detail:
      if user.username == username:
        return user

  @classmethod
  def user_exist(cls, username):
    '''
    method that checks if a username exists from account list
    '''  
    for user in cls.user_detail:
      if user.username == username:
        return True
        
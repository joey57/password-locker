import unittest
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviors

  Args:
     unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    set up method to run before each test case
    '''
    self.new_user = User("facebook", "watdavid", "123jm" , "123jm")

  def tearDown(self):
    '''
    tearDown method does clean up after each test case has run.
    '''  
    User.user_detail = []
 
  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.account_name,"facebook")
    self.assertEqual(self.new_user.username,"watdavid") 
    self.assertEqual(self.new_user.password,"123jm") 
    self.assertEqual(self.new_user.confirm_password,"123jm")

  def test_save_detail(self):
    '''
    test-save-detail test case to test if the detail of the user is saved into user detail list
    '''    
    self.new_user.save_detail()
    self.assertEqual(len(User.user_detail),1)

  def test_save_multiple_detail(self):
    '''
    test-save-multiple-detail to check if we can save multiple user objects to our user-detail list
    '''  
    self.new_user.save_detail()
    test_user = User("Test", "user", "123jm","123jm")
    test_user.save_detail()
    self.assertEqual(len(User.user_detail),2)

  def test_delete_detail(self):
    '''
    test_delete_detial to test if we can remove user detail from our user detail list
    '''  
    self.new_user.save_detail()
    test_user = User("Test", "user", "123jm","123jm")
    test_user.save_detail()
    self.new_user.delete_detail()
    self.assertEqual(len(User.user_detail),1)

  def test_display_all_details(self):
    '''
    test_display_all_details test case returns a list of all user details that are saved
    '''  
    self.assertEqual(User.display_all_details(),User.user_detail)

  def test_find_username(self):
    '''
    test to check if we can find an account using username
    '''  
    self.new_user.save_detail()

    test_user = User("test","user","3456t", "3456t")
    test_user.save_detail()

    found_user = User.find_by_username("user")
    self.assertEqual(found_user.username,test_user.username)

  # def test_user_exist(self):
  #   '''
  #   test to check if we can return a boolean if we can not finds the account
  #   '''
  #   self.new_user.save_detail()
  #   test_account = User("Test","account","jk25","jk25")
  #   test_account.save_detail()
    
  #   user_exists = User.user_exist("account_name")
  #   self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()    
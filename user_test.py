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
    self.new_user = User("Facebook" , "James")
 
  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.login_account,"Facebook")
    self.assertEqual(self.new_user.login_username,"James")  

  def test_save_detail(self):
    '''
    test-save-detail test case to test if the detail of the user is saved into user detail list
    '''    
    self.new_user.save_detail()
    self.assertEqual(len(User.user_detail),1)

if __name__ == '__main__':
    unittest.main()    
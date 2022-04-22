import unittest
from credential import Credentials

class TestCredential(unittest.TestCase):
  '''
  Test class that defines test cases for the contact class behaviours
  Args:
       unnittest.Testcase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    setUp method to run before each test cases.
    '''
    self.new_password = Credentials("jjsquared")

  def test_init_(self):
    '''
    test_init_ test case to test if the object is initialized properly
    '''  
    self.assertEqual(self.new_password.credential_detail,"jjsquared")

if __name__ == '__main__':
    unittest.main()
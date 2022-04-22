import unittest
from credential import Credential

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the contact class behaviours
  Args:
       unnittest.Testcase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    setUp method to run before each test cases.
    '''
    self.new_credential = Credential("jjsquared")

    if __name__ == '__main__':
     unittest.main()
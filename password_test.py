import unittest
from password import User
from password import Credentilas

class TestUser(unittest.TestCase):
  """
  Test class that defines  test cases for user class
  """
  def setUp(self):
    """
    method to run before each test
    """
    self.new_user = User("Chelsea", "12345")
  def tearDown(self):
    """
    tearDown method that does clean up after each case has run.
    """
    User.user_list = []
    
  def test_init(self):
    """
    test_init test case to test if the object is initialized properly 
    """
    self.assertEqual(self.new_user.username, "Chelsea")
    self.assertEqual(self.new_user.password, "12345")
    
  def test_save_user(self):
    """
    saving user details
    """
    self.new_user.save_user()
    self.assertEqual(len(User.user_list), 1)  
    
class TestCredentials(unittest.TestCase):
  def setUp(self):
    """
    method to run before each test
    """
    self.new_account = Credentilas("Flab","flab123","1234")
    
  def tearDown(self):
    """
    tearDown method that does clean up after each case has run.
    """
    Credentilas.account_list = []
    
  def test_init(self):
    """
    test_init test case to test if the object is initialized properly 
    """
    self.assertEqual(self.new_account.sitename, "Flab")
    self.assertEqual(self.new_account.accountname, "flab123")
    self.assertEqual(self.new_account.password, "1234")
    
  def test_save_account(self):
    """
    saving account details
    """
    self.new_account.save_account()
    self.assertEqual(len(Credentilas.account_list), 1)
    
  def test_save_many_accounts(self):
    """
    saving multiple accounts
    """
    self.new_account.save_account()
    test_account = Credentilas("Flab", "flab123", "1234") 
    test_account.save_account()
    self.assertEqual(len(Credentilas.account_list),2)
    
  def test_delete_account(self):
    """
    deleting account details
    """
    self.new_account.save_account()
    test_account = Credentilas("Flab", "flab123", "1234")
    test_account.save_account()
    
    self.new_account.delete_account()
    self.assertEqual(len(Credentilas.account_list),1)
  
  def test_display_credentials(self):
    """
    displaying credentials
    """
    self.assertEqual(Credentilas.display_account(),Credentilas.account_list)      
      
if __name__ == '__main__':
  unittest.main()

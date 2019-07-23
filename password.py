class User:
  """
  class containing user details
  """
  user_list = [] #empty login list
  def __init__(self, username, password):
    """
    creates unique details for each instance
    """
    self.username = username
    self.password = password
    
  def save_user(self):
    """
    save user details method
    """
    User.user_list.append(self) 
    
    
class Credentilas:
  """
  class containing account details
  """
  account_list = [] #empty account list
  def __init__(self, sitename, accountname, password):
    """
    Creates unique details for credentials
    """
    self.sitename = sitename
    self.accountname = accountname
    self.password = password
  
  def save_account(self):
    """
    save account credentials method
    """
    Credentilas.account_list.append(self)
    
  def delete_account(self):
    """
    delete account credentials method
    """
    Credentilas.account_list.remove(self)  
  
  @classmethod
  def display_account(cls):
    """
    display account credentials
    """
    return cls.account_list
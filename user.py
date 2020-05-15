class User:
    """ 
    This is a class for creating user instances to allow authentication. 
      
    Attributes: 
        email (string): The user's email address. 
        password (string): The user's hashed password. 
    """
    def __init__(self, email, password):
        """ 
        The constructor for User class. 
  
        Parameters: 
            email (string): The user's email address. 
            password (string): The user's hashed password.    
        """
        self.email = email
        self.password = password

    def is_authenticated(self):
        """
        States whether a user is authenticated

        Returns:
            Boolean: True or False
        """
        return True

    def is_active(self):
        """
        States whether a user is active

        Returns:
            Boolean: True or False
        """
        return True

    def is_anonymous(self):
        """
        States whether a user is anonymous

        Returns:
            Boolean: True or False
        """
        return False

    def get_id(self):
        """
        Returns the user's ID

        Returns:
            email: The user's email address
        """
        return self.email
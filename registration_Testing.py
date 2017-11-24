import unittest

Class Users(unittest.TestCase): #creating users class
        
def test_user_registeration(self): #create a function for testing user registration input in the Users class

        with self.client: 
            response = self.client.post('register/', data=dict(
                username='lisa', email='lisa@gmail.com',
                password='lisa345', confirm='lisa345'
            ), follow_redirects=True) #initializing direct values for a response using dictionary
            self.assertIn(b'Bright Events!', response.data) #verifying response code working correctly
            self.assertTrue(current_user.name == "lisa")
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='lisa@gmail.com').first() #querying from the record to make the email as unique identifier
            self.assertTrue(str(user) == '<name - lisa>') #verfying the name

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='lisa', email='lisa@gmail.com',
                password='lisa345', confirm='lisa345'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data) #verfying an invalid email
            self.assertIn(b'/register/', request.url)

    # Ensure id is correct for the current/logged in user
    def test_get_by_id(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="admin", password='admin'
            ), follow_redirects=True) #direct initialization
            self.assertTrue(current_user.id == 1) #verifying the id of the user logged in
            self.assertFalse(current_user.id == 20)#verfying false if the user does not match the Id.

    # Ensure given password is correct after unhashing
    def test_check_password(self):
        user = User.query.filter_by(email='ad@min.com').first() #checking password by checking the email first
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin')) #verfying if the password matches the users email 
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))#verfying a false password that does not match with the users email


if __name__ == '__main__':
    unittest.main()

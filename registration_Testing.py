import unittest
def test_user_registeration(self):

        with self.client:
            response = self.client.post('register/', data=dict(
                username='lisa', email='lisa@gmail.com',
                password='lisa345', confirm='lisa345'
            ), follow_redirects=True)
            self.assertIn(b'Bright Events!', response.data)
            self.assertTrue(current_user.name == "lisa")
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='lisa@gmail.com').first()
            self.assertTrue(str(user) == '<name - lisa>')

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='lisa', email='lisa@gmail.com',
                password='lisa345', confirm='lisa345'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)
            self.assertIn(b'/register/', request.url)

    # Ensure id is correct for the current/logged in user
    def test_get_by_id(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="admin", password='admin'
            ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)

    # Ensure given password is correct after unhashing
    def test_check_password(self):
        user = User.query.filter_by(email='ad@min.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))


if __name__ == '__main__':
    unittest.main()
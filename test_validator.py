import unittest
import validator

class TestValidator(unittest.TestCase):

    def test_first_name_empty(self):
        self.assertFalse(validator.is_first_name_valid(""))

    def test_first_name_valid(self):
        self.assertTrue(validator.is_first_name_valid("esmanur"))

    def test_first_name_none(self):
        self.assertFalse(validator.is_first_name_valid(None))

    def test_email_none(self):
        self.assertFalse(validator.is_email_valid(None))

    def test_email_invalid(self):
        self.assertFalse(validator.is_email_valid("testgmail.com"))

    def test_email_valid(self):
        self.assertTrue(validator.is_email_valid("test@gmail.com"))

    def test_password_none(self):
        self.assertFalse(validator.is_password_valid(None))

    def test_password_short(self):
        self.assertFalse(validator.is_password_valid("123"))

    def test_password_valid(self):
        self.assertTrue(validator.is_password_valid("123456"))

    def test_password_exact_boundary(self):
        self.assertTrue(validator.is_password_valid("123456"))

    def test_password_boundary_fail(self):
        self.assertFalse(validator.is_password_valid("12345"))

    def test_passwords_not_match(self):
        self.assertFalse(validator.passwords_match("123456", "654321"))

    def test_passwords_match(self):
        self.assertTrue(validator.passwords_match("123456", "123456"))

    def test_dob_none(self):
        self.assertFalse(validator.is_dob_valid(None))

    def test_dob_invalid(self):
        self.assertFalse(validator.is_dob_valid("12-12-2000"))

    def test_dob_valid(self):
        self.assertTrue(validator.is_dob_valid("21/09/2003"))

if __name__ == "__main__":
    unittest.main()
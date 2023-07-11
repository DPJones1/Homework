import unittest
from assignment import is_isogram

class IsIsogramTestCase(unittest.TestCase):
    def test_is_isogram_special_characters(self):
        word = "hello%%!"
        self.assertFalse(is_isogram(word), f"Expect {word} to be an isogram, please remove special characters")

        #This test would be useful so that no special characters get counted onl letters

    def test_is_isogram_numbers(self):
        word = "hi345"
        self.assertFalse(is_isogram(word), f'Expect {word} not to be isogram, please remove numbers')

        #This test will avoid counting numbers

    def test_is_isogram_empty(self):
        word = " "
        self.assertFalse(is_isogram(word), "Your input needs to contain characters")

        #This test will ensure that the user inputs something


if __name__ == '__main__':
    unittest.main()


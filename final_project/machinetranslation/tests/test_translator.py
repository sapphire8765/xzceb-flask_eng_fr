""" This module unit tests the translator module """
from logging import NullHandler
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """ This class contains functions to test the translation between English and French """
    def test_english_to_french(self):
        """
        This function tests the translation from English to French
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')

    def test_french_to_english(self):
        """
        This function tests the translation from French to English
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Goodbye')

    def test_null_english_to_french(self):
        """
        This function checks if null input was provided
        """
        self.assertEqual(english_to_french(''), 'Nothing to translate')

    def test_null_french_to_english(self):
        """
        This function checks if null input was provided
        """
        self.assertEqual(french_to_english(''), 'Nothing to translate')

if __name__=='__main__':
    unittest.main()

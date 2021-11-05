""" This module unit tests the translator module """
from logging import NullHandler
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """ This class contains functions to test the translation between English and French """
    def test_english_to_french(self):
        """
        This function unit tests the translation from English to French
        """

        self.assertEqual(english_to_french(''), 'Nothing to translate')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')

    def test_french_to_english(self):
        """
        This function unit tests the translation from French to English
        """

        self.assertEqual(french_to_english(''), 'Nothing to translate')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Goodbye')

if __name__=='__main__':
    unittest.main()

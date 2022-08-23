import unittest
from translator import english_to_french,french_to_english

class EnglishToFrench(unittest.TestCase):
    
    def test_null(self):
        self.assertNotEqual(english_to_french(''), 'error')

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')






class FrenchToEnglish(unittest.TestCase):

    def test_null(self):
        self.assertNotEqual(french_to_english(''), 'error')

    def test_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()

import unittest
from .translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):

    def test_english2french(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_french2english(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
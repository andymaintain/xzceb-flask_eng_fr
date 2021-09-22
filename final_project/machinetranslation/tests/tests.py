import unittest

from translator import french_to_english, english_to_french

class Test_frenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test for when Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english('pain'), 'Bread')  # Test for pain as input the output is bread
        self.assertEqual(french_to_english('travail'), 'Job')  #.Test for travail as input the output is work
        

class Test_englishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # . Test for Hello as input the output is Bounjour
        self.assertEqual(english_to_french('Bakery'), 'Boulangerie') # Test for bakery as input the output is boulangerie
        self.assertEqual(english_to_french('aeroplane'), 'Avion') # Test for aerroplane as input the output is avion
        
unittest.main()
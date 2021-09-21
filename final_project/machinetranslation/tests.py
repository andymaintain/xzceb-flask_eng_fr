import unittest

from translator import frenchtoenglish, englishtofrench

class Test_frenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello') # Test for when Bonjour is given as input the output is Hello.
        self.assertEqual(frenchtoenglish('pain'), 'bread')  # Test for pain as input the output is bread
        self.assertEqual(frenchtoenglish('travail'), 'work')  #.Test for travail as input the output is work
        

class Test_englishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour') # . Test for Hello as input the output is Bounjour
        self.assertEqual(englishtofrench('Bakery'), 'Boulangerie') # Test for bakery as input the output is boulangerie
        self.assertEqual(englishtofrench('aeroplane'), 'avion') # Test for aerroplane as input the output is avion
        
unittest.main()
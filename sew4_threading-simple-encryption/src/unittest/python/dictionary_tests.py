import unittest
from encryption.simpleencrypter import SimpleEncrypter


class DictionaryTests(unittest.TestCase):

    def setUp(self):
        self.__dict_upperLetters = {' ': ' ', 'A': 'V', 'B': 'J', 'C': 'Z', 'D': 'B', 'E': 'G', 'F': 'N', 'G': 'F', 'H': 'E',
                                'I': 'P', 'J': 'L', 'K': 'I', 'L': 'T', 'M': 'M', 'N': 'X', 'O': 'D', 'P': 'W', 'Q': 'K',
                                'R': 'Q', 'S': 'U', 'T': 'C', 'U': 'R', 'V': 'Y', 'W': 'A', 'X': 'H', 'Y': 'S', 'Z': 'O'}

    def tearDown(self):
        SimpleEncrypter.setCryptography({},distance=0)
        SimpleEncrypter.setMessage("")

    def test_message_simple_encryption(self):
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=3)
        SimpleEncrypter.setMessage("HELLO WORLD AND EVERYONE ELSE")
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == 'EGTTD ADQTB VXB GYGQSDXG GTUG')

    def test_message_simple_encryption1(self):
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=-3)
        SimpleEncrypter.setMessage("HELLO WORLD AND EVERYONE ELSE")
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == 'EGTTD ADQTB VXB GYGQSDXG GTUG')

    def test_message_simple_encryption2(self):
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=10)
        SimpleEncrypter.setMessage("HELLO WORLD AND EVERYONE ELSE")
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == 'EGTTD ADQTB VXB GYGQSDXG GTUG')

    def test_dictionary_almost_empty_encryption(self):
        SimpleEncrypter.setCryptography({' ':' '}, distance=0)
        M = "HELLO WORLD AND EVERYONE ELSE"
        SimpleEncrypter.setMessage(M)
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == M)

    def test_dictionary_almost_empty_encryption2(self):
        SimpleEncrypter.setCryptography({' ':' '}, distance= -1528)
        M = "HELLO WORLD AND EVERYONE ELSE"
        SimpleEncrypter.setMessage(M)
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == '0-447 ?7:4, )6, ->-:A76- -4;-')

    def test_dictionary_almost_empty_encryption3(self):
        SimpleEncrypter.setCryptography({' ':' '}, distance= -1000000)
        M = "HELLO WORLD AND EVERYONE ELSE"
        SimpleEncrypter.setMessage(M)
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == ',)003 ;360( %2( ):)6=32) )07)')

    def test_dictionary_almost_empty_encryption4(self):
        SimpleEncrypter.setCryptography({' ':' ', 'E': 'E'}, distance= -1000000)
        M = "HELLO WORLD AND EVERYONE ELSE"
        SimpleEncrypter.setMessage(M)
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage(), 'eEiil tloib _kb EsEovlkE EipE')

    def test_dictionary_upperLetters_encryption(self):
        SimpleEncrypter.setMessage(''.join((self.__dict_upperLetters).keys()))
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage(),''.join((self.__dict_upperLetters).values()))

    def test_dictionary_empty_encryption(self):
        SimpleEncrypter.setCryptography({}, distance=0)
        SimpleEncrypter.setMessage("hello world and everyone else")
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        with self.assertRaises(LookupError):
            thread.run()

    def test_message_empty_encryption(self):
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=0)
        SimpleEncrypter.setMessage("")
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        with self.assertRaises(LookupError):
            thread.run()


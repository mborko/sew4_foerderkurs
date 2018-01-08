import unittest
from encryption.crypt import Cryptography


class EncryptionTests(unittest.TestCase):

    def setUp(self):
        self.__dict_upperLetters = {' ': ' ', 'A': 'V', 'B': 'J', 'C': 'Z', 'D': 'B', 'E': 'G', 'F': 'N', 'G': 'F', 'H': 'E',
                                'I': 'P', 'J': 'L', 'K': 'I', 'L': 'T', 'M': 'M', 'N': 'X', 'O': 'D', 'P': 'W', 'Q': 'K',
                                'R': 'Q', 'S': 'U', 'T': 'C', 'U': 'R', 'V': 'Y', 'W': 'A', 'X': 'H', 'Y': 'S', 'Z': 'O'}

    def tearDown(self):
        pass

    def test_crypt_init(self):
        crypt = Cryptography("HELLO WORLD", self.__dict_upperLetters, 1, distance=1)
        self.assertTrue(crypt.getEncryptedMessage() == "EGTTD ADQTB")

    def test_crypt_setMessage(self):
        crypt = Cryptography("HELLO WORLD", self.__dict_upperLetters, 1, distance=1)
        crypt.setMessage("ABC")
        self.assertTrue(crypt.getEncryptedMessage() == "VJZ")

    def test_crypt_setThreadCount(self):
        crypt = Cryptography("HELLO WORLD", self.__dict_upperLetters, 1, distance=1)
        crypt.setThreadCount(20)
        self.assertTrue(crypt.getEncryptedMessage() == "EGTTD ADQTB")

    def test_crypt_getEncryptedMessage(self):
        crypt = Cryptography("HELLO WORLD", self.__dict_upperLetters, 1, distance=1)
        self.assertFalse(crypt.getEncryptedMessage() == "")

    def test_crypt_getEncryptedMessage1(self):
        crypt = Cryptography("HELLO WORLD", self.__dict_upperLetters, 1, distance=0)
        self.assertTrue(crypt.getEncryptedMessage() == "EGTTD ADQTB")

    def test_crypt_getEncryptedMessage2(self):
        crypt = Cryptography("HELLO WORLD", self.__dict_upperLetters, 1, distance=1)
        self.assertTrue(crypt.getEncryptedMessage() == "EGTTD ADQTB")

    def test_crypt_getEncryptedMessage3(self):
        crypt = Cryptography("Hello World", self.__dict_upperLetters, 1, distance=0)
        self.assertTrue(crypt.getEncryptedMessage() == "Eello Aorld")

    def test_crypt_getEncryptedMessage4(self):
        with self.assertRaises(TypeError):
            crypt = Cryptography({'A':'B','C':'D', 'E':'F'}, self.__dict_upperLetters, 1, distance=0)

    def test_crypt_getEncryptedMessage5(self):
        crypt = Cryptography("Hello World", self.__dict_upperLetters, 1, distance=0)
        with self.assertRaises(TypeError):
            Cryptography.setMessage({'A':'B','C':'D', 'E':'F'})

    def test_crypt_getEncryptedSet(self):
        with self.assertRaises(TypeError):
            crypt = Cryptography({'A','B','C','D', 'E','F'}, self.__dict_upperLetters, 1, distance=1)


import unittest
from encryption.simpleencrypter import SimpleEncrypter


class MessageTests(unittest.TestCase):

    def setUp(self):
        self.__dict_upperLetters = {' ': ' ', 'A': 'V', 'B': 'J', 'C': 'Z', 'D': 'B', 'E': 'G', 'F': 'N', 'G': 'F', 'H': 'E',
                                'I': 'P', 'J': 'L', 'K': 'I', 'L': 'T', 'M': 'M', 'N': 'X', 'O': 'D', 'P': 'W', 'Q': 'K',
                                'R': 'Q', 'S': 'U', 'T': 'C', 'U': 'R', 'V': 'Y', 'W': 'A', 'X': 'H', 'Y': 'S', 'Z': 'O'}

    def tearDown(self):
        # now we have to cleanup!
        SimpleEncrypter.setCryptography({},distance=0)
        SimpleEncrypter.setMessage("")

    def test_message_empty(self):
        SimpleEncrypter.setMessage("")
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        self.assertTrue(len(SimpleEncrypter.getMessage()) == 0)

    def test_message_length(self):
        message = "hello world and everyone else"
        SimpleEncrypter.setMessage(message)
        SimpleEncrypter.setCryptography("")
        self.assertTrue(len(SimpleEncrypter.getMessage()) == len(message))

    def test_message_unencrypted(self):
        message = "hello world and everyone else"
        SimpleEncrypter.setMessage(message)
        self.assertTrue(SimpleEncrypter.getMessage() == message)

    def test_message_empty_encryption(self):
        SimpleEncrypter.setMessage("")
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        with self.assertRaises(LookupError): #, message="No message set"): deprecated
            thread.run()

    def test_message_list(self):
        SimpleEncrypter.setMessage(['A','B','C','D'])
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        self.assertTrue(len(SimpleEncrypter.getMessage()) == 4)

    def test_message_list1(self):
        SimpleEncrypter.setMessage(['A','B','C','D'])
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        self.assertTrue(SimpleEncrypter.getMessage() == 'ABCD')

    def test_message_tuple(self):
        SimpleEncrypter.setMessage(('A','B','C','D', 'E'))
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        self.assertTrue(len(SimpleEncrypter.getMessage()) == 5)

    def test_message_tuple2(self):
        SimpleEncrypter.setMessage(('A','B','C','D', 'E'))
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        self.assertTrue(SimpleEncrypter.getMessage() == 'ABCDE')

    def test_message_list_run(self):
        SimpleEncrypter.setMessage(['A','B','C','D'])
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        thread = SimpleEncrypter(0, 1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "VJZB")

    def test_message_tuple_run(self):
        SimpleEncrypter.setMessage(('A','B','C','D','E'))
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        thread = SimpleEncrypter(0, 1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "VJZBG")



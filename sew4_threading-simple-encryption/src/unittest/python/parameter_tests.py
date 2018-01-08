import unittest
from threading import Thread
from encryption.simpleencrypter import SimpleEncrypter


class ParameterTests(unittest.TestCase):

    def setUp(self):
        self.__dict_upperLetters = {' ': ' ', 'A': 'V', 'B': 'J', 'C': 'Z', 'D': 'B', 'E': 'G', 'F': 'N', 'G': 'F', 'H': 'E',
                                'I': 'P', 'J': 'L', 'K': 'I', 'L': 'T', 'M': 'M', 'N': 'X', 'O': 'D', 'P': 'W', 'Q': 'K',
                                'R': 'Q', 'S': 'U', 'T': 'C', 'U': 'R', 'V': 'Y', 'W': 'A', 'X': 'H', 'Y': 'S', 'Z': 'O'}

    def tearDown(self):
        # now we have to cleanup!
        SimpleEncrypter.setCryptography({},distance=0)
        SimpleEncrypter.setMessage("")

    def test_inheritance(self):
        self.assertTrue(issubclass(SimpleEncrypter,Thread))

    def test_init_parameters_pass(self):
        thread = SimpleEncrypter(firstIndex=0, offset=3)
        thread.setMessage("ABCDEF")
        thread.setCryptography(self.__dict_upperLetters)
        thread.run()
        self.assertTrue(thread.getMessage() == "VBCBEF")

    def test_init_parameters_wrongNames(self):
        with self.assertRaises(TypeError):
            thread = SimpleEncrypter(first=0, set=3)

    def test_init_parameters_toofew(self):
        with self.assertRaises(TypeError):
            thread = SimpleEncrypter()

    def test_init_parameters_noIndex(self):
        with self.assertRaises(TypeError):
            thread = SimpleEncrypter(offset=2)

    def test_init_parameters_typeOfOffset(self):
        with self.assertRaises(TypeError):
            thread = SimpleEncrypter(firstIndex=2,offset='c')

    def test_init_parameters_typeOfIndex(self):
        with self.assertRaises(TypeError):
            thread = SimpleEncrypter(firstIndex=2.,offset=2)

    def test_init_parameters_borderFirstIndexCheck(self):
        with self.assertRaises(ValueError):
            thread = SimpleEncrypter(-2,2)

    def test_message_dict(self):
        SimpleEncrypter.setMessage({'A':'B','C':'D', 'E':'F'})
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        self.assertTrue(SimpleEncrypter.getMessage() == 'ACE')

    def test_message_dict_run(self):
        SimpleEncrypter.setMessage({'A': 'B', 'C': 'D', 'E': 'F'})
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        thread = SimpleEncrypter(0, 1)
        with self.assertRaises(TypeError):
            thread.run()


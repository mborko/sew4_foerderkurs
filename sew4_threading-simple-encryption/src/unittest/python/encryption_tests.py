import unittest
from encryption.simpleencrypter import SimpleEncrypter


class EncryptionTests(unittest.TestCase):

    def setUp(self):
        self.__dict_upperLetters = {' ': ' ', 'A': 'V', 'B': 'J', 'C': 'Z', 'D': 'B', 'E': 'G', 'F': 'N', 'G': 'F', 'H': 'E',
                                'I': 'P', 'J': 'L', 'K': 'I', 'L': 'T', 'M': 'M', 'N': 'X', 'O': 'D', 'P': 'W', 'Q': 'K',
                                'R': 'Q', 'S': 'U', 'T': 'C', 'U': 'R', 'V': 'Y', 'W': 'A', 'X': 'H', 'Y': 'S', 'Z': 'O'}

    def tearDown(self):
        # now we have to cleanup!
        SimpleEncrypter.setCryptography({},distance=0)
        SimpleEncrypter.setMessage("")

    def test_encryption_pass(self):
        thread = SimpleEncrypter(0,1)
        SimpleEncrypter.setMessage("hello")
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=0)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "hello")

    def test_encryption_pass1(self):
        thread = SimpleEncrypter(1,2)
        SimpleEncrypter.setMessage("hello")
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "hflmo")

    def test_encryption_pass2(self):
        thread = SimpleEncrypter(1,2)
        SimpleEncrypter.setMessage("HELLO")
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=0)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "HGLTO")

    def test_encryption_passDistance(self):
        SimpleEncrypter.setMessage("hello")
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=10)
        thread = SimpleEncrypter(0,1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "rovvy")

    def test_encryption_passLongDistance(self):
        SimpleEncrypter.setMessage('xyz !"#')
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=100)
        thread = SimpleEncrypter(0,1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == ":;< [\]")

    def test_encryption_passSentence(self):
        M = "I am Sir Oracle, And when I ope my lips, let no dog bark!"
        SimpleEncrypter.setMessage(M)
        SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=0)
        thread = SimpleEncrypter(0,1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "P am Uir Dracle, Vnd when P ope my lips, let no dog bark!")

    def test_encryption_passSentence1(self):
        M = "I am Sir Oracle, And when I ope my lips, let no dog bark!"
        SimpleEncrypter.setMessage(M)
        SimpleEncrypter.setCryptography({' ':'.'}, distance=0)
        thread = SimpleEncrypter(0,1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == "I.am.Sir.Oracle,.And.when.I.ope.my.lips,.let.no.dog.bark!")

    def test_encryption_passSentence2(self):
        M = "I am Sir Oracle, And when I ope my lips, let no dog bark!"
        SimpleEncrypter.setMessage(M)
        SimpleEncrypter.setCryptography({' ':'_'}, distance=1)
        thread = SimpleEncrypter(0,1)
        thread.run()
        self.assertTrue(SimpleEncrypter.getMessage() == 'J_bn_Tjs_Psbdmf-_Boe_xifo_J_pqf_nz_mjqt-_mfu_op_eph_cbsl"')

    def test_encryption_passfile(self):
        plain = open("scripts/testfile.text", "r")
        cipher = open("scripts/testfile_encrypted.text", "r")
        with plain, cipher:
            message = plain.read()
            SimpleEncrypter.setMessage(message)
            SimpleEncrypter.setCryptography(self.__dict_upperLetters, distance=10)
            thread = SimpleEncrypter(0,1)
            thread.run()
            self.assertTrue(SimpleEncrypter.getMessage() == cipher.read())

    def test_encryption_fails(self):
        thread = SimpleEncrypter(firstIndex=0, offset=1)
        SimpleEncrypter.setMessage("get rekt")
        SimpleEncrypter.setCryptography(self.__dict_upperLetters)
        thread.run()
        self.assertFalse(SimpleEncrypter.getMessage() == "FGC QGIC")



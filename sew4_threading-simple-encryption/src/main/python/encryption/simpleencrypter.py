"""
Created on 02.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171102

@description: Implementation eines einfachen Encryptors für A bis Z,
              aber auch zusätzlich für alle visible ascii chars
              in einem erweiterten Schritt
"""
import threading
import operator


class SimpleEncrypter(threading.Thread):

    message = []
    dictionary = dict()
    lock = threading.Lock()
    decryption = False

    def __init__(self, firstIndex, offset):
        threading.Thread.__init__(self)
        self.__firstIndex = firstIndex
        self.__offset = offset

    @staticmethod
    def setCryptography(dictionary, distance=0, decryption=False): #changed parameter name dict to dic1 since dict is a reserved word
        SimpleEncrypter.dictionary = dictionary
        SimpleEncrypter.setDecryption(decryption)

    @staticmethod
    def setDecryption(enabled):
        if operator.xor(SimpleEncrypter.decryption, enabled):
            # https://stackoverflow.com/questions/7360757/reversing-dictionary-in-python
            dict(map(reversed, SimpleEncrypter.dictionary.items()))
            SimpleEncrypter.decryption = not SimpleEncrypter.decryption
        print(SimpleEncrypter.dictionary)

    @staticmethod
    def setMessage(message):
        SimpleEncrypter.message = list(message)

    @staticmethod
    def getMessage():
        return ''.join(SimpleEncrypter.message)

    def run(self):
        # en/decrypt message through dictionary mapping
        i = self.__firstIndex
        while i < len(SimpleEncrypter.message):
            with SimpleEncrypter.lock:
                SimpleEncrypter.message[i] = SimpleEncrypter.dictionary[SimpleEncrypter.message[i]]
            # TODO not sure if we have do add 1
            i += self.__offset

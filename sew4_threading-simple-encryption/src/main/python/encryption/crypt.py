"""
Created on 02.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171102

@description: Implementation eines einfachen Encryptors für A bis Z,
              aber auch zusätzlich für alle visible ascii chars in einem erweiterten Schritt
"""
from encryption.simpleencrypter import SimpleEncrypter


class Cryptography():

    def __init__(self, message, dictionary, threads, distance=0):
        if isinstance(message, (dict, set)):
            raise TypeError()
        self.__message = message
        self.__secretDictionary = dictionary
        self.__threadcount = threads
        self.__distance = distance


    def setDictionary(self,dictionary):
        self.__secretDictionary = dictionary

    def setMessage(self,message):
        if isinstance(message, (dict, set)):
            raise TypeError()
        self.__message = message

    def setThreadCount(self,threads):
        self.__threadcount = threads

    def getEncryptedMessage(self):
        SimpleEncrypter.setMessage(self.__message)

        threads = []
        for i in range(0, self.__threadcount):
            thread = SimpleEncrypter(i, self.__threadcount)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()

        return SimpleEncrypter.getMessage()

    def getDecryptedMessage(self):
        SimpleEncrypter.setDecryption(True)
        threads = []
        for i in range(0, self.__threadcount):
            thread = SimpleEncrypter(i, self.__threadcount)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()

        return SimpleEncrypter.getMessage()


def main():
    message = input("Give me please the message for encryption: ")
    threads = input("How many threads do you want to start? ")
    dictionary = {' ': ' ', 'A': 'V', 'B': 'J', 'C': 'Z', 'D': 'B', 'E': 'G', 'F': 'N', 'G': 'F',
                                'H': 'E',
                                'I': 'P', 'J': 'L', 'K': 'I', 'L': 'T', 'M': 'M', 'N': 'X', 'O': 'D', 'P': 'W',
                                'Q': 'K',
                                'R': 'Q', 'S': 'U', 'T': 'C', 'U': 'R', 'V': 'Y', 'W': 'A', 'X': 'H', 'Y': 'S',
                                'Z': 'O'}
    crypt = Cryptography(message, dictionary, threads)
    encryptedMessage = crypt.getEncryptedMessage()
    print("Your encrypted message: " + encryptedMessage )

    decryptedMessage = crypt.getDecryptedMessage()
    print('Your decrypted message: %s' % decryptedMessage)


if  __name__ == '__main__':
    main()


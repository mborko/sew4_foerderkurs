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
        pass

    def getDecryptedMessage(self):
        pass

def main():
    decryptedMessage = crypt.getDecryptedMessage()
    print('Your decrypted message: %s' % decryptedMessage)

#if  __name__ == '__main__':
#    main()


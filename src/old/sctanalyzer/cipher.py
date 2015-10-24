"""
This module provides a Cipher base class used by SCTAnalyzer for decrypt
ciphers and generating keys.
"""

class Cipher(object):
    """
    A base class for concrete Cipher classes providing methods for
    ciphertext decryption and key generation.
    """
    def decrypt(self, ciphertext, key):
        """
        Decrypt _ciphertext_ using key _key_.
        """
        raise NotImplementedError


    def initialkey(self, ciphertext, langdata):
        """
        Guess initial key based on the given ciphertext and language data.
        """
        raise NotImplementedError


    def neighbourhood(self, key, ciphertext, langdata):
        """
        Get neighbourhood of given key.
        """
        raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()


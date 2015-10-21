"""
This module provides implementation of CaesarCipher class used for Caesar
cipher decryption.
"""

from permutation import Permutation
from cipher import Cipher

class CaesarCipher(Cipher):
    """
    A concrete Cipher implementation for Caesar cipher.
    """
    def decrypt(self, ciphertext, key):
        return Permutation.shift(-key)(ciphertext)


    def initialkey(self, ciphertext, langdata):
        freq = [0] * 26
        mostFrequent = max((v,k) for k, v in langdata.ngrams(1).items())[1]
        for c in ciphertext:
                freq[ord(c) - ord(mostFrequent)] += 1
        return max((f, c) for c, f in enumerate(freq))[1]


    def neighbourhood(self, key, ciphertext, langdata):
        for i in range(0, 26):
            yield i


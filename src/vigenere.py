class Vigenere:
    """
    An implementation of Vigeneres cipher.
    """
    _ASIZE = ord('Z') - ord('A') + 1

    _START = ord('A')

    @classmethod
    def encode(cls, plaintext, key):
        """
        Encode _plaintext_ using _key_.

        >>> Vigenere.encode('THOMASJEFFERSON', 'PET')
        'ILHBELYIYUIKHSG'
        """
        return cls._trans(plaintext.upper(), key, cls._encchar)

    @classmethod
    def decode(cls, ciphertext, key):
        """
        Decode _ciphertext using _key_.

        >>> Vigenere.decode('ILHBELYIYUIKHSG', 'PET')
        'THOMASJEFFERSON'
        """
        return cls._trans(ciphertext.upper(), key, cls._decchar)

    @classmethod
    def _trans(cls, text, key, encfunc):
        k = len(key)
        return ''.join(encfunc(c, key[i % k]) for i, c in enumerate(text))

    @classmethod
    def _modad(cls, c, k):
        c += (1 - 2*(c>0)) * cls._START
        k += (1 - 2*(k>0)) * cls._START
        return cls._START + (c + k) % cls._ASIZE

    @classmethod
    def _encchar(cls, c, k):
        return chr(cls._modad(ord(c), ord(k)))

    @classmethod
    def _decchar(cls, c, k):
        return chr(cls._modad(ord(c), -ord(k)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()


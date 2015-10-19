class Vigenere:
    """
    An implementation of Vigeneres cipher.
    """
    _ASIZE = ord('Z') - ord('A') + 1

    _START = ord('A')

    def encode(plaintext, key):
        """
        Encode _plaintext_ using _key_.

        >>> Vigenere.encode('THOMASJEFFERSON', 'PET')
        'ILHBELYIYUIKHSG'
        """
        return Vigenere._trans(plaintext.upper(), key, Vigenere._encchar)

    def decode(ciphertext, key):
        """
        Decode _ciphertext using _key_.

        >>> Vigenere.decode('ILHBELYIYUIKHSG', 'PET')
        'THOMASJEFFERSON'
        """
        return Vigenere._trans(ciphertext.upper(), key, Vigenere._decchar)

    def _trans(text, key, encfunc):
        k = len(key)
        return ''.join(encfunc(c, key[i % k]) for i, c in enumerate(text))

    def _modad(c, k):
        c += (1 - 2*(c>0)) * Vigenere._START
        k += (1 - 2*(k>0)) * Vigenere._START
        return Vigenere._START + (c + k) % Vigenere._ASIZE

    def _encchar(c, k):
        return chr(Vigenere._modad(ord(c), ord(k)))

    def _decchar(c, k):
        return chr(Vigenere._modad(ord(c), -ord(k)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()


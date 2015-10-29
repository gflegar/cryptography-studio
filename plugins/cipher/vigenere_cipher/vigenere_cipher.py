from plugins.cipher.cipher import Cipher
from plugins.cipher.vigenere_cipher.widget import PluginController


class VigenereCipher(Cipher):
    """
    An implementation of Vigeneres cipher.
    """
    _ASIZE = ord('Z') - ord('A') + 1
    _START = ord('A')

    def __init__(self, parent):
        self._parent = parent
        self._plugin_controller = None

    def encrypt(self, plaintext, key):
        """
        Encrypt _plaintext_ using _key_.

        >>> VigenereCipher().encrypt('THOMASJEFFERSON', 'PET')
        'ILHBELYIYUIKHSG'
        """
        return ''.join(self._trans(plaintext, key, self._encchar))

    def decrypt(self, ciphertext, key):
        """
        Decrypt _ciphertext using _key_.

        >>> VigenereCipher().decrypt('ILHBELYIYUIKHSG', 'PET')
        'THOMASJEFFERSON'
        """
        return ''.join(self._trans(ciphertext, key, self._decchar))

    def get_widget(self):
        if self._plugin_controller is None:
            self._plugin_controller = PluginController(self._parent, self)
        return self._plugin_controller.get_widget()

    @classmethod
    def _trans(cls, text, key, encfunc):
        key = key.upper()
        k = len(key)
        kp = 0
        for i, c in enumerate(text.upper()):
            if ord('A') <= ord(c) <= ord('Z'):
                yield encfunc(c, key[kp])
                kp = (kp + 1) % k
            else:
                yield c

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


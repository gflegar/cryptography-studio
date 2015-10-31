"""
This module provides Cipher definition for Vigenere's cipher.
"""


from plugins.cipher.cipher import Cipher
from plugins.cipher.vigenere_cipher.widget import PluginController


class VigenereCipher(Cipher):
    """
    An implementation of Vigeneres cipher.
    """

    _ASIZE = ord('Z') - ord('A') + 1
    _START = ord('A')

    def __init__(self, parent):
        """ Create a new VigenereCipher instance.

        Args:
            parent: a class that provides an interface to CryptographyStudio
        """
        self._parent = parent
        self._plugin_controller = None

    def encrypt(self, plaintext, key):
        """ Encrypt the given text.

        Args:
            plaintext: string, text to encrypt
            key: strin, key used for encryption

        Returns:
            String containing encrypted text.

        >>> VigenereCipher().encrypt('THOMASJEFFERSON', 'PET')
        'ILHBELYIYUIKHSG'
        """
        return ''.join(self._trans(plaintext, key, self._encchar))

    def decrypt(self, ciphertext, key):
        """ Decrypt the given text.

        Args:
            ciphertext: string, text to decrypt
            key: string, key used for decryption

        Returns:
            String containing decrypted text.

        >>> VigenereCipher().decrypt('ILHBELYIYUIKHSG', 'PET')
        'THOMASJEFFERSON'
        """
        return ''.join(self._trans(ciphertext, key, self._decchar))

    def get_widget(self):
        """ Get the widget for this cipher.

        Returns:
            A Gtk.Widget used to control this plugin.
        """
        if self._plugin_controller is None:
            self._plugin_controller = PluginController(self._parent, self)
        return self._plugin_controller.get_widget()

    @classmethod
    def _trans(cls, text, key, encfunc):
        """ Transform each letter of the given text.

        i-th letter is transformed by using (i mod len(key))-th letter of the
        key.

        Args:
            text: string, text to transform
            key: string, key used for transformation
            encfunct: function used for transformation -- it must receive a
                text letter and a key letter as input and return a transformed
                letter
        """
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
        """ Add ASCII values of two letters in a maner defined by Vigenere's
        cipher.

        Args:
            c: an integer ASCII value of uppercase english letter
            k: another integer ASCII value of uppercase english letter

        Returns:
            ASCII value of the resulting character.
        """
        c += (1 - 2*(c>0)) * cls._START
        k += (1 - 2*(k>0)) * cls._START
        return cls._START + (c + k) % cls._ASIZE

    @classmethod
    def _encchar(cls, c, k):
        """ Encrypt a character with the given key character.

        Args:
            c: an uppercase english letter
            k: an uppsercase english letter used as a key

        Return:
            Resulting encrypted letter.
        """
        return chr(cls._modad(ord(c), ord(k)))

    @classmethod
    def _decchar(cls, c, k):
        """ Decrypt a character with the given key character.

        Args:
            c: an uppercase english letter
            k: an uppsercase english letter used as a key

        Return:
            Resulting decrypted letter.
        """
        return chr(cls._modad(ord(c), -ord(k)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


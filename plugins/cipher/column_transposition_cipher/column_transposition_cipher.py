"""
This module provides Cipher definition for column transposition cipher.
"""


from plugins.cipher.cipher import Cipher
from plugins.cipher.column_transposition_cipher.widget import PluginController


class ColumnTranspositionCipher(Cipher):
    """
    An implementation of column transposition cipher.
    """

    _CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, parent):
        """ Create a new ColumnTranspositionCipher instance.

        Args:
            parent: a class that provides an interface to CryptographyStudio
        """
        self._parent = parent
        self._plugin_controller = None
        self.set_fill_char("X")

    def encrypt(self, plaintext, key):
        """ Encrypt the given text.

        Args:
            plaintext: string, text to encrypt
            key: list, key used for encryption

        Returns:
            String containing encrypted text.
        """
        square = self.make_square(plaintext, len(key))
        return ''.join(self.transpose(square, self.inverse(key)))

    def decrypt(self, ciphertext, key):
        """ Decrypt the given text.

        Args:
            ciphertext: string, text to decrypt
            key: list, key used for decryption

        Returns:
            String containing decrypted text.
        """
        ln = int(len(ciphertext) / len(key))
        square = [ciphertext[i:i+ln] for i in range(0, len(ciphertext), ln)]
        return self.read_square(self.transpose(square, key))

    def get_widget(self):
        """ Get the widget for this cipher.

        Returns:
            A Gtk.Widget used to control this plugin.
        """
        if self._plugin_controller is None:
            self._plugin_controller = PluginController(self._parent, self)
        return self._plugin_controller.get_widget()

    def set_fill_char(self, char):
        self._fill_char = char[0]

    def make_square(self, text, dim):
        sqr = [''] * dim
        i = 0
        j = 0
        while i < len(text) or j % dim != 0:
            if i >= len(text) or text[i].upper() in self._CHARS:
                sqr[j % dim] += text[i] if i < len(text) else self._fill_char
                j += 1
            i += 1
        return sqr

    @classmethod
    def read_square(cls, square):
        return ''.join(''.join(s) for s in zip(*square))

    @classmethod
    def transpose(cls, square, key):
        return [square[i] for i in key]

    @classmethod
    def inverse(cls, key):
        inv_key = [0] * len(key)
        for i, k in enumerate(key):
            inv_key[k] = i
        return inv_key

if __name__ == "__main__":
    import doctest
    doctest.testmod()


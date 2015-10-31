""" This module provides Cipher definition for the simple substitution cipher.
"""


from plugins.cipher.cipher import Cipher
from plugins.cipher.substitution_cipher.widget import PluginController


class SubstitutionCipher(Cipher):
    """
    This is a Cipher implementation for the simple substitution cipher.
    """

    def __init__(self, parent):
        """ Create a new SubstitutionCipher instance.

        Args:
            parent: a class that provides an interafce to CryptographyStudio
        """
        self._parent = parent
        self._plugin_controller = None

    def encrypt(self, plaintext, key):
        """ Encrypt the given text.

        Args:
            plaintext: string, text to encrypt
            key: Permutation, key used for encryption

        Returns:
            String containing encrypted text.
        """
        return key(plaintext)

    def decrypt(self, ciphertext, key):
        """ Decrypt the given text.

        Args:
            ciphertext: string, text to decrypt
            key: key used for decryption

        Returns:
            String containing decrypted text.
        """
        return (~key)(ciphertext)

    def get_widget(self):
        """ Get the widget for this cipher.

        Returns:
            A Gtk.Widget used to control this plugin.
        """
        if self._plugin_controller is None:
            self._plugin_controller = PluginController(self._parent, self)
        return self._plugin_controller.get_widget()


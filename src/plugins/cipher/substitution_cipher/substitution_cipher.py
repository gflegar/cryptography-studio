"""
This module provides Cipher definition for the general substitution cipher.
"""


from plugins.cipher.cipher import Cipher
from plugins.cipher.substitution_cipher.widget import PluginController


class SubstitutionCipher(Cipher):
    """
    This is a Cipher implementation for the general substitution cipher.
    """
    def __init__(self, parent):
        self._parent = parent
        self._plugin_controller = None

    def encrypt(self, plaintext, key):
        return key(plaintext)

    def decrypt(self, ciphertext, key):
        return (~key)(ciphertext)

    def get_widget(self):
        if self._plugin_controller is None:
            self._plugin_controller = PluginController(self._parent, self)
        return self._plugin_controller.get_widget()


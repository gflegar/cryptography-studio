""" This module defines the ABC for all cipher-type plugins. """


import abc


class Cipher(metaclass=abc.ABCMeta):
    """ An ABC for cipher plugins.

    All cipher plugins should extend this class.
    """
    @abc.abstractmethod
    def __init__(self, parent):
        """ Create a new Cipher instance.

        Args:
            parent: a class that provides an interface to CryptographyStudio
        """
        pass

    @abc.abstractmethod
    def encrypt(self, plaintext, key):
        """ Encrypt the given text.

        Args:
            plaintext: string, text to encrypt
            key: key used for encryption

        Returns:
            String containing encrypted text.
        """
        pass

    @abc.abstractmethod
    def decrypt(self, ciphertext, key):
        """ Decrypt the given text.

        Args:
            ciphertext: string, text to decrypt
            key: key used for decryption

        Returns:
            String containing decrypted text.
        """
        pass


    @abc.abstractmethod
    def get_widget(self):
        """ Get the widget for this cipher.

        Returns:
            A Gtk.Widget used to control this plugin.
        """
        pass


"""
This module provides a WidgetController for ColumnTranspositionCipher.
"""


from os import path


from cstudio import widget_controller


class PluginController(widget_controller.WidgetController):
    """ This is a WidgetController for the column transposition cipher plugin.

    """
    GLADE_LOCATION = path.dirname(__file__)
    KEY_ENTRY_ID = "key_entry"
    ENCRYPT_BUTTON_ID = "encrypt_button"
    DECRYPT_BUTTON_ID = "decrypt_button"

    def __init__(self, parent, cipher):
        """ Create a new PluginController instance.

        Args:
            parent: a clas providing interface to Cryptography Studio core
            cipher: a VigenereCipher instance used for encryption and
                decryption
        """
        super().__init__(parent)
        self._cipher = cipher
        self._widget.show_all()

    def _load_gui_objects(self):
        """ Save references to required objects defined in the .glade file. """
        super()._load_gui_objects()
        self._encrypt_button = self._builder.get_object(self.ENCRYPT_BUTTON_ID)
        self._decrypt_button = self._builder.get_object(self.DECRYPT_BUTTON_ID)
        self._key_entry = self._builder.get_object(self.KEY_ENTRY_ID)

    def _connect_handlers(self):
        """ Connect signals with their handler methods. """
        super()._connect_handlers()
        self._encrypt_button.connect("clicked", self._encrypt)
        self._decrypt_button.connect("clicked", self._decrypt)

    def _encrypt(self, *args):
        """ A handler method that encrypts the text inside the parent's text
        view when the encrypt button is clicked.

        Args:
            *args: arguments passed to this handler
        """
        key = self._get_key(self._key_entry.get_text())
        print(key)
        self._transform_parent_text(
                lambda x: self._cipher.encrypt(x, key))

    def _decrypt(self, *args):
        """ A handler method that decrypts the text inside the parent's text
        view when the decrypt button is clicked.

        Args:
            *args: arguments passed to this handler
        """
        key = self._get_key(self._key_entry.get_text())
        self._transform_parent_text(
                lambda x: self._cipher.decrypt(x, key))

    def _get_key(self, key_string):
        key = [int(n) - 1 for n in key_string.split()]
        for i, j in enumerate(sorted(key)):
            if i != j:
                return [0]
        if not key:
            return [0]
        return key

    def _transform_parent_text(self, transform):
        """ Transform the parent's text with the given transformation.

        Args:
            transform: a callable that transforms the given text, it should
                receive a single string as input and return the trasformed
                string
        """
        self._parent.set_text(transform(self._parent.get_text()))


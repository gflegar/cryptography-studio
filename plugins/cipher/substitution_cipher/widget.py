""" This module provides a WidgetController for SubstitutionCipher. """


from os import path


from cstudio import widget_controller
from plugins.cipher.substitution_cipher.permutation_selector\
    import PermutationSelector
from plugins.utils.permutation import Permutation


class PluginController(widget_controller.WidgetController):
    """ This is a WidgetController for the substitution cipher plugin.

    It provides a permutation selector implemented by PermutationSelector class
    as well as encrypt and decrypt buttons that encrypt and decrypt a given
    text.

    Class attributes:
        GLADE_LOCATION: string, nme of the .galde file for UI
        SETTINGS_BOX_ID: string, id of the container for the
            PermutationSelector widget
        ENCRYPT_BUTTON_ID: string, id of the encrypt button
        DECRYPT_BUTTON_ID: string, id of the decrypt button
    """
    GLADE_LOCATION = path.dirname(__file__)
    SETTINGS_BOX_ID = "settings_box"
    ENCRYPT_BUTTON_ID = "encrypt_button"
    DECRYPT_BUTTON_ID = "decrypt_button"

    def __init__(self, parent, cipher):
        """ Create a new PluginController instance.

        Args:
            parent: a clas providing interface to Cryptography Studio core
            cipher: a SubstitutionCipher instance used for encryption and
                decryption
        """
        super().__init__(parent)
        self._cipher = cipher
        self._widget.show_all()

    def _build_gui(self):
        """ Build the widget UI of this PluginController. """
        super()._build_gui()
        settings_box = self._builder.get_object(self.SETTINGS_BOX_ID)
        self._permutation_selector = PermutationSelector()
        settings_box.pack_start(self._permutation_selector, True, False, 0)

    def _load_gui_objects(self):
        """ Save references to required objects defined in the .glade file. """
        super()._load_gui_objects()
        self._encrypt_button = self._builder.get_object(self.ENCRYPT_BUTTON_ID)
        self._decrypt_button = self._builder.get_object(self.DECRYPT_BUTTON_ID)

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
        permutation = self._permutation_selector.get_permutation()
        self._transform_parent_text(
                lambda x: self._cipher.encrypt(x, permutation))

    def _decrypt(self, *args):
        """ A handler method that decrypts the text inside the parent's text
        view when te decrypt button is clicked.

        Args:
            *args: arguments passed to this handler
        """
        permutation = self._permutation_selector.get_permutation()
        self._transform_parent_text(
                lambda x: self._cipher.decrypt(x, permutation))

    def _transform_parent_text(self, transform):
        """ Transform the parent's text with the given transformation.

        Args:
            transform: a callable that transforms the given text, it should
                receive a single string as input and return the trasformed
                string
        """
        self._parent.set_text(transform(self._parent.get_text()))


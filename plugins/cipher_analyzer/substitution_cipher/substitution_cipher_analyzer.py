""" This module provides a CipherAnalyzer for the simple substitution cipher.

It is based on the widget for the SubstitutionCipher and currently doesn't add
any special functionalities.
"""


from os import path


from cstudio.widget_controller import WidgetController
from plugins.cipher_analyzer.cipher_analyzer import CipherAnalyzer
from plugins.cipher.substitution_cipher.substitution_cipher\
    import SubstitutionCipher
from plugins.cipher.substitution_cipher.permutation_selector\
    import PermutationSelector
#from plugins.utils.permutation import Permutation


class SubstitutionCipherAnalyzer(WidgetController, CipherAnalyzer):
    """
    This is a Cipher Analyzer implementation for the simple substitution
    cipher.

    Args:
        GLADE_LOCATION: string, path to de "resources" folder containing the
            .glade file for this widget
        SETTINGS_BOX_ID: string, id of the container in which the cipher
            selection widget is placed
        TRY_BUTTON_ID: string, id of the try button
    """
    GLADE_LOCATION = path.dirname(__file__)
    SETTINGS_BOX_ID = "settings_box"
    TRY_BUTTON_ID = "try_button"

    def __init__(self, parent):
        """ Create a new SubstitutionCipherAnalyzer instance.

        Args:
            parent: a class that provides an interafce to CryptographyStudio
        """
        super().__init__(parent)
        self._cipher = SubstitutionCipher(parent)
        self._widget.show_all()

    def _build_gui(self):
        """ Build the widget UI of this WidgetController. """
        super()._build_gui()
        settings_box = self._builder.get_object(self.SETTINGS_BOX_ID)
        self._permutation_selector = PermutationSelector()
        settings_box.pack_start(self._permutation_selector, True, False, 0)

    def _load_gui_objects(self):
        """ Save references to required objects defined in the .glade file. """
        super()._load_gui_objects()
        self._try_button = self._builder.get_object(self.TRY_BUTTON_ID)

    def _connect_handlers(self):
        """ Connect signals with their handler methods. """
        super()._connect_handlers()
        self._try_button.connect("clicked", self._try_key)

    def _try_key(self, *args):
        """ A handler method that trys to decrypt the text in the parents
        ciphertext view.

        Key is obtained from this widget's PermutationSelector and the result
        is displayed in parent's plaitext view.

        Args:
            *arg: arguments passed from the signal
        """
        key = self._permutation_selector.get_permutation()
        ciphertext = self._parent.get_ciphertext()
        self._parent.set_plaintext(self._cipher.decrypt(ciphertext, key))


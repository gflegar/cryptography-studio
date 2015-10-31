""" This module provides a WidgetController that controlls the Encrypt/Decrypt
tab of Cryptography Studio.
"""


from cstudio.widget_controller import WidgetController
from cstudio.plugin_selector import PluginSelector


class EncryptDecryptController(WidgetController):
    """ The EncryptDecryptController class controlls the Encrypt/Decrypt tab of
    Cryptography Studio.

    It provides a Gtk.TextView used for entering plaintext/ciphertext and a
    PluginSelector that allows selection of various cipher plugins for
    encryption and decryption.

    Class attributes:
        GLADE: string, name of the .glade file for UI
        WIDGET_ID: string, id of the parent widget in GLADE
        LABEL_ID: string, id of the widget used as a tab label
        TEXT_VIEW_ID: string, id of the Gtk.TextView for plaintext/ciphertext
        CIPHER_WINDOW_ID: string, id of the widget container containing the
            PluginSelector widget
        PLUGINS_PACKAGE: string, name of the plugin type offered in the
            PluginSelector
    """

    GLADE = "encode_decode.glade"
    WIDGET_ID = "encode_decode_note"
    LABEL_ID = "encode_decode_note_label"
    TEXT_VIEW_ID = "text_view"
    CIPHER_WINDOW_ID = "cipher_window"
    PLUGINS_PACKAGE = "cipher"

    def __init__(self, plugin_controller):
        """ Create a new EncryptDecryptController instance.

        Args:
            plugin_controller: A PluginController used to load the cipher
                plugin
        """
        super().__init__()
        self._plugin_controller = plugin_controller
        self._cipher_selector = PluginSelector(self, self._plugin_controller)
        self._cipher_selector.populate(self.PLUGINS_PACKAGE)
        self._cipher_window.add(self._cipher_selector.get_widget())
        self._widget.show_all()

    def get_label(self):
        """ Get the tab label widget.

        Returns:
            A Gtk.Widget that should be used as a tab label.
        """
        return self._label

    def get_text(self):
        """ Get the text from the plaintext/ciphertext TextView.

        Returns:
            A string containing text from the TextView.
        """
        start = self._text_buffer.get_start_iter()
        end = self._text_buffer.get_end_iter()
        return self._text_buffer.get_text(start, end, False)

    def set_text(self, text):
        """ Set the text in plaintext/ciphertext TextView.

        Args:
            text: string, text to set in the TextView
        """
        self._text_buffer.set_text(text)

    def _load_gui_objects(self):
        """ Save references to key objects defined in the .glade file to local
        attributes.
        """
        super()._load_gui_objects()
        self._label = self._builder.get_object(self.LABEL_ID)
        text_view = self._builder.get_object(self.TEXT_VIEW_ID)
        self._text_buffer = text_view.get_buffer()
        self._cipher_window = self._builder.get_object(self.CIPHER_WINDOW_ID)


""" This module provides a WidgetController for controlling the Analyze tab of
CryptographyStudio. """


from cstudio.widget_controller import WidgetController
from cstudio.plugin_selector import PluginSelector


class AnalyzeController(WidgetController):
    """ The AnalyzeController class controls the Analyze tab of
    CryptographyStudio.

    It provides two Gtk.TextViews, one for ciphertext and one for decoded
    plaintext. It also has two placeholders for plugins, one for language and
    the other for cipher analyzer.

    Class attributes:
        GLADE: string, name of the .glade file for UI
        WIDGET_ID: string, id of the parent widget in GLADE
        LABEL_ID: string, id of the wiget used as a tab label
        CIPHERTEXT_VIEW_ID: string, id of the Gtk.TextView for ciphertext
        PLAINTEXT_VIEW_ID: string, id of the Gtk.TextView for plaintext
        CIPHER_WINDOW_ID: string, id of the placeholder for cipher analyzer
            PluginSelector
        LANGUAGE_WINDOW_ID: string, id of the placeholder for language analyzer
            PluginSelector
        CIPHER_ANALYZER_PACKAGE: name of the plugin type for cipher analyzer
            plugins
        LANGUAGE_ANALYZER_PACKAGE: name of the plugin type for language anlyzer
            plugins
    """

    GLADE = "analyze.glade"
    WIDGET_ID = "analyze_note"
    LABEL_ID = "analyze_note_label"
    CIPHERTEXT_VIEW_ID = "ciphertext_view"
    PLAINTEXT_VIEW_ID = "plaintext_view"
    CIPHER_WINDOW_ID = "cipher_window"
    LANGUAGE_WINDOW_ID = "language_analyzer_window"
    CIPHER_ANALYZER_PACKAGE = "cipher_analyzer"
    LANGUAGE_ANALYZER_PACKAGE = "language_analyzer"

    def __init__(self, plugin_controller):
        """ Create a new AnalyzeController instance.

        Args:
            plugin_controller: A PluginController used to load the cipher and
                language analyzer plugins
        """
        super().__init__()
        self._plugin_controller = plugin_controller
        self._cipher_selector = PluginSelector(self, self._plugin_controller)
        self._cipher_selector.populate(self.CIPHER_ANALYZER_PACKAGE)
        self._cipher_window.add(self._cipher_selector.get_widget())
        self._language_selector = PluginSelector(self, self._plugin_controller)
        self._language_selector.populate(self.LANGUAGE_ANALYZER_PACKAGE)
        self._language_window.add(self._language_selector.get_widget())
        self._widget.show_all()

    def get_label(self):
        """ Get the tab label widget.

        Returns:
            A Gtk.Widget that should be used as a tab label.
        """
        return self._label

    def get_ciphertext(self):
        """ Get the text from the ciphertext TextView.

        Returns:
            A string containing text from the TextView
        """
        return self._get_text_from_buffer(self._ciphertext_buffer)

    def get_plaintext(self):
        """ Get the text from the plaintext TextView.

        Returns:
            A string containing text from the TextView
        """
        return self._get_text_from_buffer(self._plaintext_buffer)

    def set_ciphertext(self, text):
        """ Set the text in ciphertext TextView.

        Args:
            text: string, text to set in the TextView
        """
        self._ciphertext_buffer.set_text(text)

    def set_plaintext(self, text):
        """ Set the text in plaintext TextView.

        Args:
            text: string, text to set in the TextView
        """
        self._plaintext_buffer.set_text(text)

    def _get_text_from_buffer(self, buffer_):
        """ Gets the text from a Gtk.TextBuffer.

        Args:
            buffer_: a Gtk.Text buffer from which the text should be extracted

        Returns:
            A string containing text from the buffer.
        """
        start = buffer_.get_start_iter()
        end = buffer_.get_end_iter()
        return buffer_.get_text(start, end, False)

    def _load_gui_objects(self):
        """ Save references to key objects defined in the .glade file to local
        attributes.
        """
        super()._load_gui_objects()
        self._label = self._builder.get_object(self.LABEL_ID)
        self._cipher_window = self._builder.get_object(self.CIPHER_WINDOW_ID)
        self._language_window = self._builder.get_object(
                self.LANGUAGE_WINDOW_ID)
        self._ciphertext_view = self._builder.get_object(
                self.CIPHERTEXT_VIEW_ID)
        self._ciphertext_buffer = self._ciphertext_view.get_buffer()
        self._plaintext_view = self._builder.get_object(
                self.PLAINTEXT_VIEW_ID)
        self._plaintext_buffer = self._plaintext_view.get_buffer()


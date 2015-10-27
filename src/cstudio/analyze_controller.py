from cstudio.widget_controller import WidgetController
from cstudio.plugin_selector import PluginSelector


class AnalyzeController(WidgetController):
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
        return self._label

    def get_ciphertext(self):
        return self._get_text_from_buffer(self._ciphertext_buffer)

    def get_plaintext(self):
        return self._get_text_from_buffer(self._plaintext_buffer)

    def set_ciphertext(self, text):
        self._ciphertext_buffer.set_text(text)

    def set_plaintext(self, text):
        self._plaintext_buffer.set_text(text)

    def _get_text_from_buffer(self, buffer_):
        start = buffer_.get_start_iter()
        end = buffer_.get_end_iter()
        return buffer_.get_text(start, end, False)

    def _load_gui_objects(self):
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


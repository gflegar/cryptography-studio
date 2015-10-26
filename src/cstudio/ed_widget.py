from gi.repository import Gtk
from os import path


from cstudio.widget_controller import WidgetController
from cstudio.plugin_selector import PluginSelector


class EncodeDecodeController(WidgetController):
    GLADE = "encode_decode.glade"
    WIDGET_ID = "encode_decode_note"
    LABEL_ID = "encode_decode_note_label"
    TEXT_VIEW_ID = "text_view"
    CIPHER_WINDOW_ID = "cipher_window"
    PLUGINS_PACKAGE = "cipher"

    def __init__(self, plugin_controller):
        super().__init__()
        self._plugin_controller = plugin_controller
        self._cipher_selector = PluginSelector(self, self._plugin_controller)
        self._cipher_selector.populate(self.PLUGINS_PACKAGE)
        self._cipher_window.add(self._cipher_selector.get_widget())
        self._widget.show_all()

    def get_label(self):
        return self._label

    def get_text(self):
        start = self._text_buffer.get_start_iter()
        end = self._text_buffer.get_end_iter()
        return self._text_buffer.get_text(start, end, False)

    def set_text(self, text):
        self._text_buffer.set_text(text)

    def _load_gui_objects(self):
        super()._load_gui_objects()
        self._label = self._builder.get_object(self.LABEL_ID)
        text_view = self._builder.get_object(self.TEXT_VIEW_ID)
        self._text_buffer = text_view.get_buffer()
        self._cipher_window = self._builder.get_object(self.CIPHER_WINDOW_ID)

    def _connect_handlers(self):
        super()._connect_handlers()
        self._text_buffer.connect("changed", self._on_text_change)

    def _on_text_change(self, widget):
        #TODO: Change when event system is implemented
        print(self.get_text())


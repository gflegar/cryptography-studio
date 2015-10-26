from gi.repository import Gtk


from cstudio.plugin_selector import PluginSelector


class EncodeDecodeController(object):
    NAMES = {
        "text_view" : "text_view",
        "cipher_widget_frame" : "cipher_widget_frame",
        "cipher_selector" : "cipher_selector",
        "cipher_plugins_package" : "cipher"
    }

    def __init__(self, builder, plugin_controller):
        self._plugin_controller = plugin_controller
        self._cipher_selector = PluginSelector(
                self, builder, self._plugin_controller,
                self.NAMES["cipher_widget_frame"],
                self.NAMES["cipher_selector"])
        self._cipher_selector.populate_selector(
                self.NAMES["cipher_plugins_package"])
        self._load_gui_objects(builder)
        self._connect_handlers()

    def get_text(self):
        start = self._text_buffer.get_start_iter()
        end = self._text_buffer.get_end_iter()
        return self._text_buffer.get_text(start, end, False)

    def set_text(self, text):
        self._text_buffer.set_text(text)

    def _load_gui_objects(self, builder):
        text_view = builder.get_object(self.NAMES["text_view"])
        self._text_buffer = text_view.get_buffer()

    def _connect_handlers(self):
        self._text_buffer.connect("changed", self._on_text_change)

    def _on_text_change(self, widget):
        #TODO: Change when event system is implemented
        print(self.get_text())


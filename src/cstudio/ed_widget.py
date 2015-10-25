from gi.repository import Gtk

class EncodeDecodeController(object):
    NAMES = {
        "text_view" : "text_view",
        "cipher_widget_frame" : "cipher_widget_frame",
        "cipher_selector" : "cipher_selector"
    }

    def __init__(self, builder, plugin_controller):
        self._load_gui_objects(builder)
        self._connect_handlers()
        self._populate_selector(plugin_controller)

    def get_text(self):
        start = self._text_buffer.get_start_iter()
        end = self._text_buffer.get_end_iter()
        return self._text_buffer.get_text(start, end, False)

    def set_text(self, text):
        self._text_buffer.set_text(text)

    def _load_gui_objects(self, builder):
        text_view = builder.get_object(self.NAMES["text_view"])
        self._text_buffer = text_view.get_buffer()
        self._cipher_selector = builder.get_object(
                self.NAMES["cipher_selector"])
        self._cipher_widget_frame = builder.get_object(
                self.NAMES["cipher_widget_frame"])
        self._cipher_list = self._cipher_selector.get_model()

    def _connect_handlers(self):
        self._cipher_selector.connect("changed", self._on_cipher_change)
        self._text_buffer.connect("changed", self._on_text_change)

    def _populate_selector(self, plugin_controller):
        #TODO: Change once the plugin_controller is implemented
        #for widget in plugin_controller.get_cipher_widgets(CipherWidget):
        #    self._cipher_list.append(widget)
        self._cipher_list.append(["My Cipher", 0])
        self._cipher_list.append(["Caesar cipher", 1])

    def _on_cipher_change(self, widget):
        #TODO: Change when plugin system is implemented
        active_iter = widget.get_active_iter()
        cipher_name = self._cipher_list.get_value(active_iter, 0)
        print("cipher changed to {}".format(cipher_name))

    def _on_text_change(self, widget):
        #TODO: Change when event system is implemented
        print(self.get_text())


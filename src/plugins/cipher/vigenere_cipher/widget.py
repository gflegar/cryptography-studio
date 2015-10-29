from os import path


from cstudio import widget_controller


class PluginController(widget_controller.WidgetController):
    GLADE_LOCATION = path.dirname(__file__)
    KEY_ENTRY_ID = "key_entry"
    ENCRYPT_BUTTON_ID = "encrypt_button"
    DECRYPT_BUTTON_ID = "decrypt_button"

    def __init__(self, parent, cipher):
        super().__init__(parent)
        self._cipher = cipher
        self._widget.show_all()

    def _load_gui_objects(self):
        super()._load_gui_objects()
        self._encrypt_button = self._builder.get_object(self.ENCRYPT_BUTTON_ID)
        self._decrypt_button = self._builder.get_object(self.DECRYPT_BUTTON_ID)
        self._key_entry = self._builder.get_object(self.KEY_ENTRY_ID)

    def _connect_handlers(self):
        super()._connect_handlers()
        self._encrypt_button.connect("clicked", self._encrypt)
        self._decrypt_button.connect("clicked", self._decrypt)

    def _encrypt(self, *args):
        key = self._key_entry.get_text()
        self._transform_parent_text(
                lambda x: self._cipher.encrypt(x, key))

    def _decrypt(self, *args):
        key = self._key_entry.get_text()
        self._transform_parent_text(
                lambda x: self._cipher.decrypt(x, key))

    def _transform_parent_text(self, transform):
        self._parent.set_text(transform(self._parent.get_text()))


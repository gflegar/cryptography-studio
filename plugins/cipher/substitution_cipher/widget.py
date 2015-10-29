from os import path


from cstudio import widget_controller
from plugins.cipher.substitution_cipher.permutation_selector\
    import PermutationSelector
from plugins.utils.permutation import Permutation


class PluginController(widget_controller.WidgetController):
    GLADE_LOCATION = path.dirname(__file__)
    SETTINGS_BOX_ID = "settings_box"
    ENCRYPT_BUTTON_ID = "encrypt_button"
    DECRYPT_BUTTON_ID = "decrypt_button"

    def __init__(self, parent, cipher):
        super().__init__(parent)
        self._cipher = cipher
        self._widget.show_all()

    def _build_gui(self):
        super()._build_gui()
        settings_box = self._builder.get_object(self.SETTINGS_BOX_ID)
        self._permutation_selector = PermutationSelector()
        settings_box.pack_start(self._permutation_selector, True, False, 0)

    def _load_gui_objects(self):
        super()._load_gui_objects()
        self._encrypt_button = self._builder.get_object(self.ENCRYPT_BUTTON_ID)
        self._decrypt_button = self._builder.get_object(self.DECRYPT_BUTTON_ID)

    def _connect_handlers(self):
        super()._connect_handlers()
        self._encrypt_button.connect("clicked", self._encrypt)
        self._decrypt_button.connect("clicked", self._decrypt)

    def _encrypt(self, *args):
        permutation = self._permutation_selector.get_permutation()
        self._transform_parent_text(
                lambda x: self._cipher.encrypt(x, permutation))

    def _decrypt(self, *args):
        permutation = self._permutation_selector.get_permutation()
        self._transform_parent_text(
                lambda x: self._cipher.decrypt(x, permutation))

    def _transform_parent_text(self, transform):
        self._parent.set_text(transform(self._parent.get_text()))


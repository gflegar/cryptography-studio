from os import path


from cstudio import widget_controller
from plugins.cipher.substitution_cipher.permutation_bit import PermutationBit
from plugins.utils.permutation import Permutation


class PluginController(widget_controller.WidgetController):
    GLADE_LOCATION = path.dirname(__file__)

    def __init__(self, parent, cipher):
        super().__init__(parent)
        self._cipher = cipher
        self._widget.show_all()
        self._toggled = []

    def _build_gui(self):
        super()._build_gui()
        box = self._builder.get_object("permutation_box")
        self._bits = []
        for char in Permutation.CHARS:
            self._bits.append(PermutationBit(char))
            box.pack_start(self._bits[-1], False, False, 0)
            self._bits[-1].connect("toggled", self._record_toggle,
                                   len(self._bits) - 1)

    def _record_toggle(self, button, button_id):
        self._toggled.append(button_id)
        if len(self._toggled) == 2:
            i1, i2 = self._toggled
            b1, b2 = self._bits[i1].get_bit(), self._bits[i2].get_bit()
            self._bits[i1].set_bit(b2)
            self._bits[i2].set_bit(b1)
            self._bits[i1].set_active(False)
            self._bits[i2].set_active(False)
            self._toggled = []

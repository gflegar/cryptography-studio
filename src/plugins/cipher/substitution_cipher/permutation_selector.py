from gi.repository import Gtk


from plugins.cipher.substitution_cipher.permutation_bit import PermutationBit
from plugins.utils.permutation import Permutation


class PermutationSelector(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(True, halign = Gtk.Align.CENTER, *args, **kwargs)
        self._build_gui()
        self._toggled = []

    def get_permutation(self):
        return Permutation(bit.get_bit() for bit in self._bits)

    def set_permutation(self, permutation):
        for i, c in enumerate(str(permutation)):
            self._bits[i].set_bit(c)

    def apply_permutation(self, permutation):
        self.set_permutation(permutation @ self.get_permutation())

    def _build_gui(self):
        self._bits = []
        for char in Permutation.CHARS:
            self._bits.append(PermutationBit(char))
            self.pack_start(self._bits[-1], False, False, 0)
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

from gi.repository import Gtk
import math


from plugins.cipher.substitution_cipher.permutation_bit import PermutationBit
from plugins.utils.permutation import Permutation


class PermutationSelector(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(
                halign = Gtk.Align.CENTER,
                orientation = Gtk.Orientation.VERTICAL,
                *args, **kwargs)
        self._build_gui()
        self._connect_handlers()
        self._toggled = []
        self._refresh_key()

    def get_permutation(self):
        return Permutation(bit.get_bit() for bit in self._bits)

    def set_permutation(self, permutation):
        for i, c in enumerate(str(permutation)):
            self._bits[i].set_bit(c)
        self._refresh_key()

    def apply_permutation(self, permutation):
        self.set_permutation(self.get_permutation() @ permutation)

    def apply_permutation_end(self, permutation):
        self.set_permutation(permutation @ self.get_permutation())

    def _build_gui(self):
        self.pack_start(self._create_permutation_box(), False, False, 3)
        self.pack_start(self._create_key_box(), False, False, 3)
        self.pack_start(self._create_affine_box(), False, False, 3)

    def _create_permutation_box(self):
        permutation_box = Gtk.Box(halign = Gtk.Align.CENTER)
        self._bits = []
        self._left_shift = Gtk.Button(valign = Gtk.Align.CENTER)
        self._left_shift.add(Gtk.Image(stock = "gtk-go-back"))
        self._right_shift = Gtk.Button(valign = Gtk.Align.CENTER)
        self._right_shift.add(Gtk.Image(stock = "gtk-go-forward"))
        selection_box = Gtk.Box(True, halign = Gtk.Align.CENTER)
        for box in (self._left_shift, selection_box, self._right_shift):
            permutation_box.pack_start(box, False, False, 0)
        for char in Permutation.CHARS:
            self._bits.append(PermutationBit(char))
            selection_box.pack_start(self._bits[-1], False, True, 1)
        return permutation_box

    def _create_key_box(self):
        self._key_entry = Gtk.Entry(
                placeholder_text = "Key",
                secondary_icon_stock = "gtk-apply")
        return self._key_entry

    def _create_affine_box(self):
        affine_box = Gtk.Box()
        mult_field = Gtk.ComboBoxText()
        add_field = Gtk.ComboBoxText()
        self._affine_button = Gtk.Button("Set", valign = Gtk.Align.CENTER)
        for item in (mult_field, Gtk.Label("X"), Gtk.Label("+"), add_field):
            affine_box.pack_start(item, False, False, 1)

        for i in range(0, len(Permutation.CHARS)):
            if math.gcd(i, len(Permutation.CHARS)) == 1:
                mult_field.append_text(str(i))
            add_field.append_text(str(i))

        affine_box.pack_start(self._affine_button, False, False, 1)
        frame = Gtk.Frame(
                label = "Affine cipher:",
                shadow_type = Gtk.ShadowType.NONE)
        frame.add(affine_box)
        self._mult_field = mult_field
        self._add_field = add_field
        return frame

    def _connect_handlers(self):
        for i, bit in enumerate(self._bits):
            bit.connect("toggled", self._record_toggle, i)
        self._left_shift.connect("clicked", self._translate, 1)
        self._right_shift.connect("clicked", self._translate, -1)
        self._key_entry.connect("icon-release", self._set_key)
        self._affine_button.connect("clicked", self._set_affine)

    def _translate(self, widget, amount):
        self.apply_permutation(Permutation.shift(amount))

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
            self._refresh_key()

    def _refresh_key(self):
        self._key_entry.set_text(str(self.get_permutation()))

    def _set_key(self, entry, icon_pos, event):
        self.set_permutation(Permutation.from_key(entry.get_text()))

    def _set_affine(self, *args):
        mult = int(self._mult_field.get_active_text())
        add = int(self._add_field.get_active_text())
        self.set_permutation(Permutation.affine(mult, add))


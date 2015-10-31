""" This module implements a PermutationSelector widget used as part of the
plugin's user interface.
"""


from gi.repository import Gtk
import math


from plugins.cipher.substitution_cipher.permutation_bit import PermutationBit
from plugins.utils.permutation import Permutation


class PermutationSelector(Gtk.Box):
    """ This is a widget that allows the user to chose a permutation of letters
    used as a key for the simple permutation cipher.
    """

    def __init__(self, *args, **kwargs):
        """ Create a new permutation selector widget.

        It delegates provided arguments to the Gtk.Box constructor.

        Args:
            *args: list containing provided arguments
            **kwagrs: dictionary containing provided keyword arguments
        """
        super().__init__(
                halign = Gtk.Align.CENTER,
                orientation = Gtk.Orientation.VERTICAL,
                *args, **kwargs)
        self._build_gui()
        self._connect_handlers()
        self._toggled = []
        self._refresh_key()

    def get_permutation(self):
        """ Get the currently selected permutation.

        Returns:
            A Permutaion instance.
        """
        return Permutation(bit.get_bit() for bit in self._bits)

    def set_permutation(self, permutation):
        """ Change the permutation displayed by this widget.

        Args:
            permutation: A permutation instance that should be displayed.
        """
        for i, c in enumerate(str(permutation)):
            self._bits[i].set_bit(c)
        self._refresh_key()

    def apply_permutation(self, permutation):
        """ Composed a permutation with the currently selected permutation
        by first applying the new permutation and then the selected one.

        Args:
            permutation: A permutation instance to compose the selected
                permutation with
        """
        self.set_permutation(self.get_permutation() @ permutation)

    def apply_permutation_end(self, permutation):
        """ Compose a permutation with thr currently selected permutation by
        first applying the selected permutation and then the new one.

        Args:
            permutation: A permutation instance to compose the selected
                permutation with
        """
        self.set_permutation(permutation @ self.get_permutation())

    def _build_gui(self):
        """ Build the UI of this widget. """
        self.pack_start(self._create_permutation_box(), False, False, 3)
        self.pack_start(self._create_key_box(), False, False, 3)
        self.pack_start(self._create_affine_box(), False, False, 3)

    def _create_permutation_box(self):
        """ Create the permutation selection box. """
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
        """ Create the key entry box. """
        self._key_entry = Gtk.Entry(
                placeholder_text = "Key",
                secondary_icon_stock = "gtk-apply")
        return self._key_entry

    def _create_affine_box(self):
        """ Create a selector for affine ciphers. """
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
        """ Connect signals with their handler methods. """
        for i, bit in enumerate(self._bits):
            bit.connect("toggled", self._record_toggle, i)
        self._left_shift.connect("clicked", self._translate, 1)
        self._right_shift.connect("clicked", self._translate, -1)
        self._key_entry.connect("icon-release", self._set_key)
        self._affine_button.connect("clicked", self._set_affine)

    def _translate(self, widget, amount):
        """ A handler method that aplies a translation to the selected
        permutation.

        Args:
            widget: widget that trigered the event
            amount: numnber of position to translate for
        """
        self.apply_permutation(Permutation.shift(amount))

    def _record_toggle(self, button, button_id):
        """ A handler that records the toggle of a permutation selection button
        and exchanges two elements if two buttons are selected.

        Args:
            button: widget that trigered the event
            button_id: position of the button in the button list
        """
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
        """ Set the current permutation in the key entry box. """
        self._key_entry.set_text(str(self.get_permutation()))

    def _set_key(self, entry, icon_pos, event):
        """ Generate current permutation from the key entry box.

        Args:
            entry: the key entry widget that trigered the event
            icon_pos: position of the icon that trigered the event
            event: the event that trigered this handler
        """
        self.set_permutation(Permutation.from_key(entry.get_text()))

    def _set_affine(self, *args):
        """ Generate current permutation from entries in the affine box.

        Args:
            *args: arguments provided by the signal
        """
        mult = int(self._mult_field.get_active_text())
        add = int(self._add_field.get_active_text())
        self.set_permutation(Permutation.affine(mult, add))


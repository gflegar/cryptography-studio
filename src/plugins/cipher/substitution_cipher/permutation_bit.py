from gi.repository import Gtk


class PermutationBit(Gtk.Box):
    def __init__(self, bit_position, *args, **kwargs):
        super().__init__(
                orientation = Gtk.Orientation.VERTICAL,
                expand = False,
                *args,
                **kwargs)
        self.add(Gtk.ToggleButton(bit_position,
            active = True,
            sensitive = False))
        self.add(Gtk.Image(stock = "gtk-go-down"))
        self._button = Gtk.ToggleButton(bit_position)
        self.add(self._button)

    def set_bit(self, bit):
        self._button.set_label(bit)

    def get_bit(self):
        return self._button.get_label()

    def set_active(self, is_active):
        self._button.set_active(is_active)

    def connect(self, *args, **kwargs):
        return self._button.connect(*args, **kwargs)


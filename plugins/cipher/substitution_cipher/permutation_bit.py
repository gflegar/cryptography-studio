""" This module provides a PermutationBit widget which is a basic building
block for the PermutationSelector widget. """


from gi.repository import Gtk


class PermutationBit(Gtk.Box):
    """ The PermutationBit widget is a single cell used for construction of the
    permutation selector widget. """

    def __init__(self, bit_position, *args, **kwargs):
        """ Create a new PermutationBit.

        Args:
            bit_position: a letter defining the position of this bit in the
                permutation -- this letter is displayed in the upper portion of
                the widget
            *args: arguments passed to the underlaying Gtk.Box widget
            *kwargs: keyword arguments passed to the underlaying Gtk.Box widget
        """
        super().__init__(
                orientation = Gtk.Orientation.VERTICAL,
                *args,
                **kwargs)
        self.add(Gtk.ToggleButton(bit_position,
            active = True,
            sensitive = False))
        self.add(Gtk.Image(stock = "gtk-go-down"))
        self._button = Gtk.ToggleButton(bit_position)
        self.add(self._button)

    def set_bit(self, bit):
        """ Set the letter displayed by the widget.

        Args:
            bit: a letter to display in the lower part of the widget
        """
        self._button.set_label(bit)

    def get_bit(self):
        """ Get the letter displayed by the widget.

        Returns:
            A letter displayed in the lower part of the widget.
        """
        return self._button.get_label()

    def set_active(self, is_active):
        """ Set the lower toggle button to desired state.

        Args:
            is_active: boolean denoting the new state of the button
        """
        self._button.set_active(is_active)

    def connect(self, *args, **kwargs):
        """ Connect a handler method to signals emited by the lower toggle
        button.

        Args:
            *args: arguments passed to toggle button's connect method
            **kwargs: keyword arguments passed to toggle button's connect
            method
        """
        return self._button.connect(*args, **kwargs)


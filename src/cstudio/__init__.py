from gi.repository import Gtk
from os import path


class CryptographyStudio(object):
    WINDOW_NAME = "cstudio"
    GLADE_NAME = "cstudio.glade"
    def __init__(self):
        glade_path = path.join(
                path.dirname(__file__),
                'resources',
                self.GLADE_NAME)
        builder = Gtk.Builder.new_from_file(glade_path)
        builder.connect_signals(self)
        window = builder.get_object(self.WINDOW_NAME)
        window.show_all()

    def on_cstudio_destroy(self, *args):
        Gtk.main_quit(*args)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


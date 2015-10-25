from gi.repository import Gtk
from os import path

from .ed_widget import EncodeDecodeController

class CryptographyStudio(object):
    GLADE = "cstudio.glade"
    NAMES = {
        "window" : "cstudio"
    }

    def __init__(self):
        self._build_gui()
        self._load_gui_objects(self._builder)
        self._connect_handlers()
        self._ed_controller = EncodeDecodeController(self._builder, None)
        self._window.show_all()

    def _build_gui(self):
        glade_path = path.join(path.dirname(__file__), "resources", self.GLADE)
        self._builder = Gtk.Builder.new_from_file(glade_path)

    def _load_gui_objects(self, builder):
        self._window = builder.get_object(self.NAMES["window"])

    def _connect_handlers(self):
        self._window.connect("delete-event", Gtk.main_quit)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


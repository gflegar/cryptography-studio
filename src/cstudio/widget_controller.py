from gi.repository import Gtk
from os import path


class WidgetController(object):
    GLADE = "widget.glade"
    WIDGET_ID = "widget"
    GLADE_LOCATION = path.join(path.dirname(__file__))

    def __init__(self, parent = None):
        self._parent = parent
        self._build_gui()
        self._load_gui_objects()
        self._connect_handlers()

    def get_widget(self):
        return self._widget

    def _build_gui(self):
        glade_path = path.join(self.GLADE_LOCATION, "resources", self.GLADE)
        self._builder = Gtk.Builder.new_from_file(glade_path)

    def _load_gui_objects(self):
        self._widget = self._builder.get_object(self.WIDGET_ID)

    def _connect_handlers(self):
        pass

from gi.repository import Gtk
from os import path


from cstudio.ed_widget import EncodeDecodeController
from cstudio.plugin_controller import PluginController


class CryptographyStudio(object):
    GLADE = "cstudio.glade"
    PLUGINS_PACKAGE = "plugins"
    WIDGET_ID = "cstudio"
    NOTEBOOK_ID = "notebook"

    def __init__(self):
        self._build_gui()
        self._load_gui_objects()
        self._connect_handlers()
        self._plugin_controller = PluginController(self.PLUGINS_PACKAGE)
        self._ed_controller = EncodeDecodeController(self._plugin_controller)
        self._notebook.append_page(
            self._ed_controller.get_widget(),
            self._ed_controller.get_label())
        self._widget.show_all()

    def _build_gui(self):
        glade_path = path.join(path.dirname(__file__), "resources", self.GLADE)
        self._builder = Gtk.Builder.new_from_file(glade_path)

    def _load_gui_objects(self):
        self._widget = self._builder.get_object(self.WIDGET_ID)
        self._notebook = self._builder.get_object(self.NOTEBOOK_ID)

    def _connect_handlers(self):
        self._widget.connect("delete-event", Gtk.main_quit)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


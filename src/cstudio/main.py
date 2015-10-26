from gi.repository import Gtk
from os import path


from cstudio.widget_controller import WidgetController
from cstudio.ed_widget import EncodeDecodeController
from cstudio.plugin_controller import PluginController


class CryptographyStudio(WidgetController):
    GLADE = "cstudio.glade"
    PLUGINS_PACKAGE = "plugins"
    WIDGET_ID = "cstudio"
    NOTEBOOK_ID = "notebook"

    def __init__(self):
        super().__init__()
        self._plugin_controller = PluginController(self.PLUGINS_PACKAGE)
        self._ed_controller = EncodeDecodeController(self._plugin_controller)
        self._notebook.append_page(
            self._ed_controller.get_widget(),
            self._ed_controller.get_label())
        self._widget.show_all()

    def _load_gui_objects(self):
        super()._load_gui_objects()
        self._notebook = self._builder.get_object(self.NOTEBOOK_ID)

    def _connect_handlers(self):
        super()._connect_handlers()
        self._widget.connect("delete-event", Gtk.main_quit)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


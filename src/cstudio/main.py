from gi.repository import Gtk


from cstudio.widget_controller import WidgetController
from cstudio.encrypt_decrypt_controller import EncryptDecryptController
from cstudio.analyze_controller import AnalyzeController
from cstudio.plugin_controller import PluginController


class CryptographyStudio(WidgetController):
    GLADE = "cstudio.glade"
    PLUGINS_PACKAGE = "plugins"
    WIDGET_ID = "cstudio"
    NOTEBOOK_ID = "notebook"

    def __init__(self):
        super().__init__()
        self._load_plugin_controller()
        self._load_tabs()
        self._widget.show_all()

    def _load_gui_objects(self):
        super()._load_gui_objects()
        self._notebook = self._builder.get_object(self.NOTEBOOK_ID)

    def _connect_handlers(self):
        super()._connect_handlers()
        self._widget.connect("delete-event", Gtk.main_quit)

    def _load_plugin_controller(self):
        self._plugin_controller = PluginController(self.PLUGINS_PACKAGE)

    def _load_tabs(self):
        self._ed_controller = EncryptDecryptController(self._plugin_controller)
        self._add_tab(self._ed_controller)
        self._analyze_controller = AnalyzeController(self._plugin_controller)
        self._add_tab(self._analyze_controller)

    def _add_tab(self, tab):
        self._notebook.append_page(tab.get_widget(), tab.get_label())


if __name__ == "__main__":
    import doctest
    doctest.testmod()


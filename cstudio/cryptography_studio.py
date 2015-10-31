""" This submodule provides Cryptography Studio's main entry point. """


from gi.repository import Gtk


from cstudio.widget_controller import WidgetController
from cstudio.encrypt_decrypt_controller import EncryptDecryptController
from cstudio.analyze_controller import AnalyzeController
from cstudio.plugin_controller import PluginController


class CryptographyStudio(WidgetController):
    """ This class implements application's main tabbed layout.

    It instatiates other parts of the application: Encode/Decode tab, Analyze
    tab and plugin loader.

    Class attributes:
        GLADE: string, name of the .glade file for main UI
        PLUGINS_PACKAGE: string, name of the package containing plugins
        WIDGET_ID: string, id of the parent widget in GLADE
        NOTEBOOK_ID: string, id of notebook to which tabs should be added
    """

    GLADE = "cstudio.glade"
    PLUGINS_PACKAGE = "plugins"
    WIDGET_ID = "cstudio"
    NOTEBOOK_ID = "notebook"

    def __init__(self):
        """ Create a new CryptographyStudio instance.

        Loads the UI from .glade file and show the main window.
        """
        super().__init__()
        self._load_plugin_controller()
        self._load_tabs()
        self._widget.show_all()

    def _load_gui_objects(self):
        """ Saves UI object to local variables. """
        super()._load_gui_objects()
        self._notebook = self._builder.get_object(self.NOTEBOOK_ID)

    def _connect_handlers(self):
        """ Connects signals to their handler methods. """
        super()._connect_handlers()
        self._widget.connect("delete-event", Gtk.main_quit)

    def _load_plugin_controller(self):
        """ Creates a new PluginController instance.

        This object loads all of the plugins requested by PluginSelectors.
        """
        self._plugin_controller = PluginController(self.PLUGINS_PACKAGE)

    def _load_tabs(self):
        """ Adds tabs to the main notebook layout.

        Instantiates new EncryptDecryptController and AnalyzeController
        instances and adds them to the layout.
        """
        self._ed_controller = EncryptDecryptController(self._plugin_controller)
        self._add_tab(self._ed_controller)
        self._analyze_controller = AnalyzeController(self._plugin_controller)
        self._add_tab(self._analyze_controller)

    def _add_tab(self, tab):
        """ Append a specific tab to notebook layout.

        Args:
            tab:  A WidgetController instance, also implementing a get_label()
                method that returns a Gtk.Widget which will be used as the
                tab's label.
        """
        self._notebook.append_page(tab.get_widget(), tab.get_label())


if __name__ == "__main__":
    import doctest
    doctest.testmod()


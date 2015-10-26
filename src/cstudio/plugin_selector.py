from gi.repository import Gtk
from os import path


import cstudio


class PluginSelector(object):
    GLADE = "plugin_selector.glade"
    WIDGET_ID = "plugin_frame"
    SELECTOR_ID = "plugin_selector"

    def __init__(self, parent, plugin_controller):
        self._build_gui();
        self._load_gui_objects()
        self._connect_handlers()
        self._parent = parent
        self._plugin = None
        self._plugin_controller = plugin_controller
        self._default_text = self._widget.get_child().get_text()

    def get_widget(self):
        return self._widget

    def populate(self, plugin_type):
        self._plugin_type = plugin_type
        self._widget.get_child().destroy()
        self._widget.add(Gtk.Label(self._default_text.format(plugin_type)))
        plugins = self._plugin_controller.get_plugins(plugin_type)
        for plugin in plugins:
            self._selection_list.append([plugin])

    def _build_gui(self):
        glade_path = path.join(path.dirname(__file__), "resources", self.GLADE)
        self._builder = Gtk.Builder.new_from_file(glade_path)

    def _load_gui_objects(self):
        self._widget = self._builder.get_object(self.WIDGET_ID)
        self._selector = self._builder.get_object(self.SELECTOR_ID)
        self._selection_list = self._selector.get_model()

    def _connect_handlers(self):
        self._selector.connect("changed", self._change_plugin)

    def _change_plugin(self, widget):
        active_iter = widget.get_active_iter()
        plugin_name = self._selection_list.get_value(active_iter, 0)
        try:
            self._plugin = self._plugin_controller.get_plugin(
                    self._plugin_type, plugin_name)(self._parent)
            print("plugin changed to {}".format(plugin_name))
            plugin_widget = self._plugin.get_widget()
        except cstudio.Error:
            plugin_widget = Gtk.Label("Unable to load {} plugin: {}".format(
                self._plugin_type, plugin_name))
        self._widget.get_child().destroy()
        self._widget.add(plugin_widget)
        plugin_widget.show()


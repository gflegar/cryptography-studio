from gi.repository import Gtk


import cstudio


class PluginSelector(object):
    def __init__(self, parent, builder, plugin_controller, frame_name,
                 selector_name):
        self._parent = parent
        self._plugin = None
        self._plugin_controller = plugin_controller
        self._load_gui_objects(builder, frame_name, selector_name)
        self._connect_handlers()

    def populate_selector(self, plugin_type):
        self._plugin_type = plugin_type
        plugins = self._plugin_controller.get_plugins(plugin_type)
        for plugin in plugins:
            self._selection_list.append([plugin])

    def _load_gui_objects(self, builder, frame_name, selector_name):
        self._frame = builder.get_object(frame_name)
        self._selector = builder.get_object(selector_name)
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
            plugin_widget = Gtk.Label("Unable to load {} plugin.".format(
                self._plugin_type))
        self._frame.get_child().destroy()
        self._frame.add(plugin_widget)
        plugin_widget.show()


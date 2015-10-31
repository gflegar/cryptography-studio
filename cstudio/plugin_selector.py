""" This module provides a simple widget for choosing a plugin of the desired
type.
"""


from gi.repository import Gtk
from os import path


import cstudio
from cstudio.widget_controller import WidgetController


class PluginSelector(WidgetController):
    """ A WidgetController that provides a widget for choosing a plugin of the
    desired type.

    It implements a simple combo-box with names of the diferent widgets and a
    scrollable area to wich the widget is loaded once te user selects a widget
    from the combo-box.

    Class attributes:
        GLADE: string, name of the .glade file for main UI
        WIDGET_ID: string, id of the parent widget in GLADE
        SELECTOR_ID: string, id of the combobox used for selecting the desired
            widget
    """

    GLADE = "plugin_selector.glade"
    WIDGET_ID = "plugin_frame"
    SELECTOR_ID = "plugin_selector"

    def __init__(self, parent, plugin_controller):
        """ Create a new PluginSelector.

        Args:
            parent: parent of this WidgetSelector
            plugin_controller: a PluginController instance used for loading
                plugins once the plugin is selected.
        """
        super().__init__(parent)
        self._plugin = None
        self._plugin_controller = plugin_controller
        self._default_text = self._widget.get_child().get_text()
        self._widget.show_all()

    def populate(self, plugin_type):
        """ Populate the selector with plugins of the given type.

        Queries the PluginController for plugins of the given type and
        populates the combo-box with it's names.

        Args:
            plugin_type: type of the plugins provided in the combo-box

        Raises:
            cstudio.Error if the plugin type doesn't exist
        """
        self._plugin_type = plugin_type
        self._widget.get_child().destroy()
        self._widget.add(Gtk.Label(
            self._default_text.format(plugin_type),
            wrap = True))
        plugins = self._plugin_controller.get_plugins(plugin_type)
        for plugin in plugins:
            self._selection_list.append([plugin])

    def _load_gui_objects(self):
        """ Save references to needed objects defined in the .glade file
        to local attributes.
        """
        super()._load_gui_objects()
        self._selector = self._builder.get_object(self.SELECTOR_ID)
        self._selection_list = self._selector.get_model()

    def _connect_handlers(self):
        """ Connect signals with their handler methods. """
        super()._connect_handlers()
        self._selector.connect("changed", self._change_plugin)

    def _change_plugin(self, widget):
        """ A handler method that loads and displays a plugin when it is
        selected.

        Args:
            widget: a selector widget that trigered the event
        """
        active_iter = widget.get_active_iter()
        plugin_name = self._selection_list.get_value(active_iter, 0)
        try:
            self._plugin = self._plugin_controller.get_plugin(
                    self._plugin_type, plugin_name)(self._parent)
            plugin_widget = self._plugin.get_widget()
        except cstudio.Error as err:
            plugin_widget = Gtk.Label("Unable to load {} plugin: {}".format(
                self._plugin_type, plugin_name))
            print(err)
        self._widget.get_child().destroy()
        self._widget.add(plugin_widget)
        plugin_widget.show_all()
        self._widget.queue_resize()


""" This module provides a PluginController class that implements Cryptography
Studio's plugin loading capabilities.
"""


import importlib
import pkgutil
import inspect


import cstudio


class PluginController(object):
    """ The PluginController class provides methods for getting information
    about available plugins and loading them into Cryptography Studio.

    Plugins are organized by type of plugin. This class can determine which
    plugins are available for the given plugin type and then dynamicly load the
    specified plugin.
    """

    def __init__(self, plugins_package):
        """ Create a new PluginController instance.

        Args:
            plugins_package: name of the package that contains all of the
                available plugins
        """
        self._plugins_package = plugins_package

    def get_plugins(self, plugin_type):
        """ Get all plugins of the specified type.

        Args:
            plugin_type: name of the plugin type (PluginController looks in a
                subpackage named `plugin_type` inside the plugins package)

        Yields:
            Names of the available plugins.

        Raises:
            cstudio.Error if it cannot find the specified plugin type.
        """
        try:
            plugins = importlib.import_module("{}.{}".format(
                self._plugins_package, plugin_type))
        except ImportError:
            raise cstudio.Error("Unknown pluigin type")
        for _, plugin_name, pkg in pkgutil.iter_modules(plugins.__path__):
            if pkg:
                yield plugin_name

    def get_plugin(self, type_, name):
        """ Return the specified plugins main class.

        Tries to load a plugin module specified by it's type and name. If
        successful it loads a class named MAIN from the module.

        Args:
            type_: type of the plugin
            name: name of the plugin

        Returns:
            Plugin's MAIN class.

        Raises:
            cstudio.Error if plugin wasn't found, doesn't have a MAIN class
            or it's main class doesn't implement the base class required
            by plugin type's abstract base class. It can also be raised if the
            plugin type is not found or doesn't have a base class.
        """
        try:
            plugin_module = importlib.import_module("{}.{}.{}".format(
                self._plugins_package, type_, name))
        except ImportError:
            raise cstudio.Error("Plugin not found");
        try:
            base_class = importlib.import_module("{}.{}".format(
                self._plugins_package, type_)).ABC
        except ImportError:
            raise cstudio.Error("Plugin type not found");
        except AttributeError:
            raise cstudio.Error("Plugin type doesn't have a base class")
        try:
            if not issubclass(plugin_module.MAIN, base_class):
                raise cstudio.Error("Error loading plugin")
        except AttributeError:
            raise cstudio.Error("Plugin does not provide a MAIN class")
        return plugin_module.MAIN


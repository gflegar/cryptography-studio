import importlib
import pkgutil
import inspect


import cstudio


class PluginController(object):
    def __init__(self, plugins_package):
        self._plugins_package = plugins_package

    def get_plugins(self, plugin_type):
        try:
            plugins = importlib.import_module("{}.{}".format(
                self._plugins_package, plugin_type))
        except ImportError:
            raise cstudio.Error("Unknown pluigin type")
        for _, plugin_name, pkg in pkgutil.iter_modules(plugins.__path__):
            if pkg:
                yield plugin_name

    def get_plugin(self, plugin_type, name):
        plugin_module = importlib.import_module("{}.{}.{}".format(
            self._plugins_package, plugin_type, name))
        base_class = importlib.import_module("{}.{}".format(
            self._plugins_package, plugin_type)).ABC
        if not issubclass(plugin_module.MAIN, base_class):
            raise cstudio.Error("Error loading plugin")
        return plugin_module.MAIN


""" This package contains various plugins for Cryptography Studio.

Plugins are organized in subpackages by plugin types (cipher analyzers,
language analyzers, etc.). Each package defines a base class ABC for all of
it's plugins that defines the interface of the plugin towards the rest of the
application.

Every plugin defines all of it's modules in a single subpackage of it's plugin
type's package and should provide a MAIN class that is a subclass of it's
plugin type's ABC class.

There is also a special subpackage called utils that is not regarded as a
plugin type package, but is instead used to provide utility modules shared
between multiple plugins.

The overall structure of the plugin package is the following:
plugins
 |-> __init__.py (<- this file)
 |-> plugin_type_1
 |    |-> __init__.py
 |    |    |-> class ABC
 |    |-> concrete_plugin_1
 |    |    |-> __init__.py
 |    |    |    |-> class MAIN
 |    |    ...
 |    |-> concrete_plugin_2
 |    |    |-> __init__.py
 |    |    |    |-> class MAIN
 |    |    ...
 |    ...
 |-> plugin_type_2
 |    |-> __init__.py
 |    |    |-> class ABC
 |    |-> concrete_plugin_3
 |    |    |-> __init__.py
 |    |    |    |-> class MAIN
 |    |    ...
 |    |-> concrete_plugin_4
 |    |    |-> __init__.py
 |    |    |    |-> class MAIN
 |    |    ...
 |    ...
 ...
 """


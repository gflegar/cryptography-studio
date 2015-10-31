""" This module define the ABC for all language analyzer plugins. """


import abc


class LanguageAnalyzer(metaclass=abc.ABCMeta):
    """ An ABC for language analyzer plugins.

    All language analyzer plugins should extend this class.
    """
    @abc.abstractmethod
    def __init__(self, parent):
        """ Create a new LanguageAnalyzer instance.

        Args:
            parent: a class that provides an interface to CryptographyStudio
        """
        pass

    @abc.abstractmethod
    def get_widget(self):
        """ Get the widget for this language analyzer.

        Returns:
            A Gtk.Widget used to control this plugin.
        """
        pass


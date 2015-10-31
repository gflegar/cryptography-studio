""" This module define the ABC for all cipher analyzer plugins. """


import abc


class CipherAnalyzer(metaclass=abc.ABCMeta):
    """ An ABC for cipher analyzer plugins.

    All cipher analyzer plugins should extend this class.
    """
    @abc.abstractmethod
    def __init__(self, parent):
        """ Create a new CipherAnalyzer instance.

        Args:
            parent: a class that provides an interface to CryptographyStudio
        """
        pass

    @abc.abstractmethod
    def get_widget(self):
        """ Get the widget for this cipher analyzer.

        Returns:
            A Gtk.Widget used to control this plugin.
        """
        pass


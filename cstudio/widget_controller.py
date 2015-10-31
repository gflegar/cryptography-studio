""" This submodule provides a base class for concrete WidgetController. """


from gi.repository import Gtk
from os import path


class WidgetController(object):
    """ A base class that automaticly does some common UI-related tasks neded
    by most classes dealing with UI manipulation.

    The class automaticly creates a Gtk.Builder object and loads the UI from a
    .glade file. It also defines and call some usefull methods from the
    constructor.

    Class attributes:
        GLADE: string, name of the .glade file for UI
        WIDGET_ID: string, id of the parent widget in GLADE
        GLADE_LOCATION: path to a folder named "resources" that contains the
            desired .glade file

    Protected attributes:
        _parent: parent of this WidgetController, provided in constructor
        _builder: a Gtk.Builder object that was used to create the GUI
        _widget: reference to the main widget in the .glade file
    """

    GLADE = "widget.glade"
    WIDGET_ID = "widget"
    GLADE_LOCATION = path.dirname(__file__)

    def __init__(self, parent = None):
        """ Create a new WidgetController instance.

        It also calls the following methods (in this particular order):
            _build_gui()
            _load_gui_objects()
            _connect_handlers()

        Args:
            parent: parent of this WidgetController
        """
        self._parent = parent
        self._build_gui()
        self._load_gui_objects()
        self._connect_handlers()

    def get_widget(self):
        """ Get the widget controlled by this WidgetController.

        Returns:
            A Gtk.Widget controlled by this WidgetController.
        """
        return self._widget

    def _build_gui(self):
        """ Build the UI from the glade file given by GLADE class attribute.
        """
        glade_path = path.join(self.GLADE_LOCATION, "resources", self.GLADE)
        self._builder = Gtk.Builder.new_from_file(glade_path)

    def _load_gui_objects(self):
        """ Save references to some of the objects defined in the .glade file
        to local attributes.

        This basic implementation saves only the parent widget.
        """
        self._widget = self._builder.get_object(self.WIDGET_ID)

    def _connect_handlers(self):
        """ Connect signals with their handler methods.

        This implementation does nothig, but is automaticly called from the
        constructor and should be overridden in subclasses to register their
        specific handlers.
        """
        pass

from os import path


from cstudio.widget_controller import WidgetController
from plugins.language_analyzer.language_analyzer import LanguageAnalyzer


class NGramAnalyzer(WidgetController, LanguageAnalyzer):
    GLADE_LOCATION = path.dirname(__file__)
    NGRAM_SELECTOR_ID = "ngram_selector"
    REFRESH_BUTTON_ID = "refresh_button"
    NGRAM_STORE_ID = "ngram_store"

    def _load_gui_objects(self):
        super()._load_gui_objects()
        self._ngram_selector = self._builder.get_object(self.NGRAM_SELECTOR_ID)
        self._refresh_button = self._builder.get_object(self.REFRESH_BUTTON_ID)
        self._ngram_store = self._builder.get_object(self.NGRAM_STORE_ID)

    def _connect_handlers(self):
        super()._connect_handlers()
        self._refresh_button.connect("clicked", self._refresh_data)
        self._ngram_selector.connect("value-changed", self._refresh_data)

    def _refresh_data(self, *args):
        print("Refresh event triggered")


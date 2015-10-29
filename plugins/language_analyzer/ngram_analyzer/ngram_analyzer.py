from os import path


from cstudio.widget_controller import WidgetController
from plugins.language_analyzer.language_analyzer import LanguageAnalyzer
from plugins.language_analyzer.ngram_analyzer.ngram_loader import NGramLoader
from plugins.utils.permutation import Permutation


class NGramAnalyzer(WidgetController, LanguageAnalyzer):
    GLADE_LOCATION = path.dirname(__file__)
    NGRAM_SELECTOR_ID = "ngram_selector"
    REFRESH_BUTTON_ID = "refresh_button"
    NGRAM_STORE_ID = "ngram_store"

    def __init__(self, parent):
        super().__init__(parent)
        self._ngram_loader = NGramLoader()

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
        #TODO: change when multiple-language support is implemented
        self._ngram_loader.load("hr.json")
        n = self._ngram_selector.get_value_as_int()
        ngrams = self._ngram_loader.get_ngrams(n)
        self._ngram_store.clear()
        try:
            max_lang = max(ngrams.values()) or 1
        except:
            max_lang = 1
        text_ngrams = self._add_plaintext_data(ngrams, n)
        try:
            max_text = max(text_ngrams.values()) or 1
        except:
            max_text = 1
        for ngram, freq in text_ngrams.items():
            lfreq = ngrams.get(ngram, 0)
            self._ngram_store.append([
                ngram,
                freq * 100 / max_text, "{:.2%}".format(freq),
                lfreq * 100 / max_lang, "{:.2%}".format(lfreq)
            ])

    def _add_plaintext_data(self, ngrams, n):
        plaintext = ''.join(char
                for char in self._parent.get_plaintext().upper()
                if char in Permutation.CHARS)
        text_ngrams = {key : 0 for key in ngrams}
        count = (len(plaintext) - n + 1) or 1
        for i in range(0, count):
            substr = plaintext[i:i+n]
            if substr in text_ngrams:
                text_ngrams[substr] += 1
            else:
                text_ngrams[substr] = 1
        for key in text_ngrams:
            text_ngrams[key] /= count
        return text_ngrams





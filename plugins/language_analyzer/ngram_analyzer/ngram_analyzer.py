""" This module provides a NGramAnalyzer class that analyzer n-gram frequencies
in decrypted text and compares them to frequencies in the selected language.
"""


from os import path


from cstudio.widget_controller import WidgetController
from plugins.language_analyzer.language_analyzer import LanguageAnalyzer
from plugins.language_analyzer.ngram_analyzer.ngram_loader import NGramLoader
from plugins.utils.permutation import Permutation


class NGramAnalyzer(WidgetController, LanguageAnalyzer):
    """ This class compares the frequencies of n-grams in the decrypted text
    and selected language and displays them in a Gtk.TreeView.

    Args:
        GLADE_LOCATION: string, path to de "resources" folder containing the
            .glade file for this widget
        NGRAM_SELECTOR_ID: string, id of the widget allowing the user to select
            the size of the n-grams (ie. "n")
        REFRESH_BUTTON_ID: string, id of the button that refreshes the widget
        NGRAM_STORE_ID: string, id of the Gtk.ListStore that holds the data
            about n-gram frequencies
    """
    GLADE_LOCATION = path.dirname(__file__)
    NGRAM_SELECTOR_ID = "ngram_selector"
    REFRESH_BUTTON_ID = "refresh_button"
    NGRAM_STORE_ID = "ngram_store"

    def __init__(self, parent):
        """ Create a new NGramAnalyzer instance.

        Args:
            parent: a class that provides an interafce to CryptographyStudio
        """
        super().__init__(parent)
        self._ngram_loader = NGramLoader()

    def _load_gui_objects(self):
        """ Save references to required objects defined in the .glade file. """
        super()._load_gui_objects()
        self._ngram_selector = self._builder.get_object(self.NGRAM_SELECTOR_ID)
        self._refresh_button = self._builder.get_object(self.REFRESH_BUTTON_ID)
        self._ngram_store = self._builder.get_object(self.NGRAM_STORE_ID)

    def _connect_handlers(self):
        """ Connect signals with their handler methods. """
        super()._connect_handlers()
        self._refresh_button.connect("clicked", self._refresh_data)
        self._ngram_selector.connect("value-changed", self._refresh_data)

    def _refresh_data(self, *args):
        """ A handler that refreshes the n-gram frequnecies of the text in the
        parent's plaintext view.

        Args:
            *args: arguments passed from the signal
        """
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
        """ Create a dictionary of ngrams and their frequencies in parent's
        plaintext view.

        Also includes all n-grams in the ngrams dictionary (with frequencies 0
        if they do not appear in the plaintext view).

        Args:
            ngrams: existing dictionary of n-grams
            n: size of the n-grams

        Returns:
            Dictionary of n-grams as keys and their frequencies as values.
        """
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





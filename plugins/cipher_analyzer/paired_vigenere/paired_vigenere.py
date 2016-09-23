"""
This module provides a CipherAnalyzer for the Vigenere cipher.
"""


from gi.repository import Gtk
from os import path


from cstudio.widget_controller import WidgetController
from plugins.cipher_analyzer.cipher_analyzer import CipherAnalyzer
from plugins.language_analyzer.ngram_analyzer.ngram_loader import NGramLoader


class PairedVigenere(WidgetController, CipherAnalyzer):
    GLADE_LOCATION = path.dirname(__file__)
    TRY_BUTTON_ID = "try_button"
    PT1_ENTRY_ID = "pt1_entry"
    PT2_ENTRY_ID = "pt2_entry"
    KEY_ENTRY_ID = "key_entry"
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, parent):
        """ Create a new VigenereCipherAnalyzer instance.

        Args:
            parent: a class that provides an interafce to CryptographyStudio
        """
        super().__init__(parent)
        self._widget.show_all()
        ngram_loader = NGramLoader()
        ngram_loader.load("hr.json")
        self._letter_freqs = ngram_loader.get_ngrams(1)

    def _load_gui_objects(self):
        """ Save references to required objects defined in the .glade file. """
        super()._load_gui_objects()
        self._try_button = self._builder.get_object(self.TRY_BUTTON_ID)
        self._pt1_entry = self._builder.get_object(self.PT1_ENTRY_ID)
        self._pt2_entry = self._builder.get_object(self.PT2_ENTRY_ID)
        self._key_entry = self._builder.get_object(self.KEY_ENTRY_ID)

    def _connect_handlers(self):
        """ Connect signals with their handler methods. """
        super()._connect_handlers()
        self._try_button.connect("clicked", self._try_key)
        self._pt1_entry.connect("changed", self._update_data)

    def _update_data(self, *args):
        tmp = self._parent.get_ciphertext().splitlines()
        while len(tmp) < 2:
            tmp.append("")
        ct1, ct2 = tmp[0].upper(), tmp[1].upper()
        pt1 = self._pt1_entry.get_text().upper()
        d = ord("A")
        num = lambda x: ord(x) - ord('A')
        tostr = lambda x: chr(x % 26 + ord('A'))
        ct1 += "A" * len(pt1)
        ct2 += "A" * len(pt1)
        key = "".join(tostr(num(y) - num(x)) for x, y in zip(pt1, ct1))
        pt2 = "".join(tostr(num(y) - num(k)) for y, k in zip(ct2, key))
        self._pt2_entry.set_text(pt2)
        self._key_entry.set_text(key)

    def _try_key(self, *args):
        """ A handler method that trys to decrypt the text in the parents
        ciphertext view.

        Args:
            *args: arguments passed from the signal
        """
        pass

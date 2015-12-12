"""
This module provides a CipherAnalyzer for the Vigenere cipher.
"""


from gi.repository import Gtk
from os import path


from cstudio.widget_controller import WidgetController
from plugins.cipher_analyzer.cipher_analyzer import CipherAnalyzer
from plugins.cipher.vigenere_cipher.vigenere_cipher\
    import VigenereCipher
from plugins.language_analyzer.ngram_analyzer.ngram_loader import NGramLoader


class VigenereCipherAnalyzer(WidgetController, CipherAnalyzer):
    GLADE_LOCATION = path.dirname(__file__)
    KEY_GLADE = "key_selector.glade"
    TRY_BUTTON_ID = "try_button"
    KEY_LENGTH_ENTRY_ID = "key_length_entry"
    KEY_SELECTOR_ID = "key_selector"
    KEY_SELECTOR_BOX_ID = "key_selector_box"
    KEY_SELECTOR_CI_ID = "ci_field"
    KEY_SELECTOR_MCI_ID = "mic_store"
    KEY_SELECTOR_MCI_VIEW = "mic_view"
    CINDEX_FIELD_ID = "coincidency_index_field"
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, parent):
        """ Create a new VigenereCipherAnalyzer instance.

        Args:
            parent: a class that provides an interafce to CryptographyStudio
        """
        super().__init__(parent)
        self._cipher = VigenereCipher(parent)
        self._widget.show_all()
        key_path = path.join(self.GLADE_LOCATION, "resources", self.KEY_GLADE)
        with open(key_path, "r") as fp:
            self._key_selector_buffer = fp.read()
        ngram_loader = NGramLoader()
        ngram_loader.load("hr.json")
        self._letter_freqs = ngram_loader.get_ngrams(1)
        self._update_key_length()

    def _build_gui(self):
        """ Build the widget UI of this WidgetController. """
        super()._build_gui()

    def _load_gui_objects(self):
        """ Save references to required objects defined in the .glade file. """
        super()._load_gui_objects()
        self._try_button = self._builder.get_object(self.TRY_BUTTON_ID)
        self._key_length_entry = \
            self._builder.get_object(self.KEY_LENGTH_ENTRY_ID)
        self._key_selector = \
        self._cindex_field = self._builder.get_object(self.CINDEX_FIELD_ID)
        self._key_selector = self._builder.get_object(self.KEY_SELECTOR_ID)

    def _connect_handlers(self):
        """ Connect signals with their handler methods. """
        super()._connect_handlers()
        self._try_button.connect("clicked", self._try_key)
        self._key_length_entry.connect("value-changed",
                self._update_key_length)

    def _update_key_length(self, *args):
        ciphertext = self._parent.get_ciphertext()
        m = int(self._key_length_entry.get_text())
        self._key_length = m
        self._create_key_selectors()
        freq = [{} for _ in range(m)]
        ttl = [0] * m
        filtered = filter(lambda x: x in self.LETTERS, ciphertext.upper())
        avg = 0
        for i, c in enumerate("".join(filtered)):
            ttl[i % m] += 1
            if c in freq[i % m]:
                freq[i % m][c] += 1
            else:
                freq[i % m][c] = 1
        for i, cs in enumerate(self._cis):
            ci = 0;
            for value in freq[i].values():
                ci += value * (value - 1)
            if ttl[i] > 1:
                ci /= ttl[i] * (ttl[i] - 1)
            else:
                ci = 0
            avg += ci
            cs.set_text(str(ci)[:5])
        self._cindex_field.set_text(str(avg/m)[:5])

    def _create_key_selectors(self):
        count = self._key_length
        for child in self._key_selector.get_children():
            child.destroy()
        selector_data = [self._create_key_selector()
                for i in range(count)]
        boxes, cis, mcis, self._mci_views = zip(*selector_data)
        self._cis, self._mcis = cis, mcis
        for box in boxes:
            self._key_selector.pack_start(box, False, False, 5)
        for i in range(len(mcis)):
            self._update_mci(i)

    def _update_mci(self, mci_id):
        ciphertext = self._parent.get_ciphertext()
        filtered = "".join(x for x in ciphertext.upper() if x in self.LETTERS)
        def mv(char, inc):
            return chr((ord(char) - ord('A') + inc) % 26 + ord('A'))
        for ind in range(len(self.LETTERS)):
            freq = {}
            ttl = 0
            for i in range(mci_id, len(filtered), self._key_length):
                fi = filtered[i]
                if fi in freq:
                    freq[fi] += 1
                else:
                    freq[fi] = 1
                ttl += 1
            mci = 0
            for l, f in self._letter_freqs.items():
                mci += f * freq.get(mv(l, ind), 0)
            if ttl > 0:
                mci /= ttl
            else:
                mci = 0
            self._mcis[mci_id].append([
                chr(ord('A') + ind),
                mci,
                int(mci * 1000)])
        self._mcis[mci_id].set_sort_column_id(1, Gtk.SortType.DESCENDING)

    def _create_key_selector(self):
        builder = Gtk.Builder.new_from_string(self._key_selector_buffer, -1)
        return (
            builder.get_object(self.KEY_SELECTOR_BOX_ID),
            builder.get_object(self.KEY_SELECTOR_CI_ID),
            builder.get_object(self.KEY_SELECTOR_MCI_ID),
            builder.get_object(self.KEY_SELECTOR_MCI_VIEW)
        )

    def _get_key(self):
        key = ''
        for mci, mci_view in zip(self._mcis, self._mci_views):
            path, column = mci_view.get_cursor()
            if not path:
                path = Gtk.TreePath.new_first()
                mci_view.set_cursor(path)
            key += mci.get(mci.get_iter(path), 0)[0]
        return key

    def _try_key(self, *args):
        """ A handler method that trys to decrypt the text in the parents
        ciphertext view.

        Args:
            *args: arguments passed from the signal
        """
        key = self._get_key()
        ciphertext = self._parent.get_ciphertext()
        self._parent.set_plaintext(self._cipher.decrypt(ciphertext, key))


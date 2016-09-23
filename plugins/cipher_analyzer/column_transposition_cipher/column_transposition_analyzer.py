"""
This module provides a CipherAnalyzer for the column transposition cipher.
"""


from gi.repository import Gtk
from os import path


from cstudio.widget_controller import WidgetController
from plugins.cipher_analyzer.cipher_analyzer import CipherAnalyzer
from plugins.cipher.column_transposition_cipher.column_transposition_cipher\
    import ColumnTranspositionCipher
from plugins.language_analyzer.ngram_analyzer.ngram_loader import NGramLoader


class ColumnTranspositionAnalyzer(WidgetController, CipherAnalyzer):
    GLADE_LOCATION = path.dirname(__file__)
    TRY_BUTTON_ID = "try_button"
    CIPHER_GRID_ID = "cipher_grid"
    KEY_ENTRY_ID = "key_entry"
    KEY_LENGTH_ENTRY_ID = "key_length_entry"
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, parent):
        """ Create a new ColumnTranspositionCipher instance.

        Args:
            parent: a class that provides an interafce to CryptographyStudio
        """
        super().__init__(parent)
        self._key_length = 1
        self._cipher = ColumnTranspositionCipher(parent)
        self._widget.show_all()
        ngram_loader = NGramLoader()
        ngram_loader.load("hr.json")
        self._bigram_freqs = ngram_loader.get_ngrams(2)
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
        self._cipher_grid = self._builder.get_object(self.CIPHER_GRID_ID)
        self._key_entry = self._builder.get_object(self.KEY_ENTRY_ID)

    def _connect_handlers(self):
        """ Connect signals with their handler methods. """
        super()._connect_handlers()
        self._try_button.connect("clicked", self._try_key)
        self._key_length_entry.connect("value-changed",
                self._update_key_length)

    def _create_grid(self):
        n = self._key_length
        for child in self._cipher_grid.get_children():
            child.destroy()
        self._grid = [[None] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                self._grid[i][j] = Gtk.ToggleButton(
                        str(self._bigram_freq(i, j))[:5])
                self._cipher_grid.attach(self._grid[i][j], i, j, 1, 1)
                self._grid[i][j].connect("toggled", self._bind_pair, i, j)
        self._cipher_grid.show_all()

    def _update_key_length(self, *args):
        ciphertext = self._parent.get_ciphertext()
        ciphertext = ''.join(filter(lambda x: x in self.LETTERS, ciphertext))
        self._calculate_key_length(len(ciphertext))
        csize = len(ciphertext) // self._key_length
        if len(ciphertext) == 0:
            self._columns = []
        else:
            self._columns = [ciphertext[i:i+csize]
                    for i in range(0, len(ciphertext), csize)]
            self._create_grid()
        self._blocks = [[i] for i in range(self._key_length)]
        self._block_assoc = list(range(self._key_length))
        self._update_display()
        """
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
        """

    def _calculate_key_length(self, ctext_length):
        nl = int(self._key_length_entry.get_text())
        if nl > ctext_length:
            nl = ctext_length if ctext_length else 1
        while ctext_length % nl != 0:
            nl += 1 if self._key_length < nl else -1
        self._key_length = nl
        self._key_length_entry.set_text(str(nl))

    def _bigram_freq(self, i, j):
        return sum(self._bigram_freqs.get(f + s, 0)
                for f, s in zip(self._columns[i], self._columns[j]))

    def _bind_pair(self, button, fst, scnd, *args):
        pass

    def _update_display(self):
        self._key_entry.set_text(
                ' '.join(map(lambda x: str(x+1), sum(self._blocks, []))))
        self._parent.set_plaintext('\n'.join(
            ''.join(a) for a in zip(*self._columns)))

    def _try_key(self, *args):
        """ A handler method that trys to decrypt the text in the parents
        ciphertext view.

        Args:
            *args: arguments passed from the signal
        """
        key = self._get_key()
        ciphertext = self._parent.get_ciphertext()
        self._parent.set_plaintext(self._cipher.decrypt(ciphertext, key))


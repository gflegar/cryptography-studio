from os import path


from cstudio.widget_controller import WidgetController
from plugins.cipher_analyzer.cipher_analyzer import CipherAnalyzer
from plugins.cipher.substitution_cipher.substitution_cipher\
        import SubstitutionCipher
from plugins.cipher.substitution_cipher.permutation_selector\
    import PermutationSelector
from plugins.utils.permutation import Permutation


class SubstitutionCipherAnalyzer(WidgetController, CipherAnalyzer):
    """
    This is a Cipher Analyzer implementation for the general substitution
    cipher.
    """
    GLADE_LOCATION = path.dirname(__file__)
    SETTINGS_BOX_ID = "settings_box"
    TRY_BUTTON_ID = "try_button"

    def __init__(self, parent):
        super().__init__(parent)
        self._cipher = SubstitutionCipher(parent)
        self._widget.show_all()

    def _build_gui(self):
        super()._build_gui()
        settings_box = self._builder.get_object(self.SETTINGS_BOX_ID)
        self._permutation_selector = PermutationSelector()
        settings_box.pack_start(self._permutation_selector, True, False, 0)

    def _load_gui_objects(self):
        super()._load_gui_objects()
        self._try_button = self._builder.get_object(self.TRY_BUTTON_ID)

    def _connect_handlers(self):
        super()._connect_handlers()
        self._try_button.connect("clicked", self._try_key)

    def _try_key(self, *args):
        key = self._permutation_selector.get_permutation()
        ciphertext = self._parent.get_ciphertext()
        print(ciphertext)
        self._parent.set_plaintext(self._cipher.decrypt(ciphertext, key))

#    def _freq2perm(self, freq):
#        """
#        Generate a permutation from a frequency table such that:
#            'A' -> min frequency
#            'Z' -> max frequency
#        """
#        flist = sorted((freq.get(l, .0), l) for l in Permutation.CHARS)
#        return Permutation(''.join(x for _, x in flist))
#
#
#    def initialkey(self, ciphertext, langdata):
#        cperm = {l : ciphertext.count(l) / len(ciphertext)
#                for l in Permutation.CHARS}
#        lperm = langdata.ngrams(1)
#        return self._freq2perm(cperm) @ ~self._freq2perm(lperm)
#
#
#    def neighbourhood(self, key, ciphertext, langdata):
#        letters = Permutation.CHARS
#        for i in range(0, len(letters)):
#            for j in range(0, i):
#                if letters[i] in ciphertext or letters[j] in ciphertext:
#                    yield Permutation.inversion(letters[i], letters[j]) @ key


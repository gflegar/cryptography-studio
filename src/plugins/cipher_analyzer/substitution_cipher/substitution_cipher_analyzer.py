from plugins.cipher_analyzer.cipher_analyzer import CipherAnalyzer
from plugins.utils.permutation import Permutation


def SubstitutionCipherAnalyzer(CipherAnalyzer):
    """
    This is a Cipher Analyzer implementation for the general substitution
    cipher.

    It uses two-element inversions for neighbourhood definition and letter
    frequency for starting state definition.
    """
    def __init__(self, parent):
        self._parent = parent

    def get_widget(self):
        return self

    def _freq2perm(self, freq):
        """
        Generate a permutation from a frequency table such that:
            'A' -> min frequency
            'Z' -> max frequency
        """
        flist = sorted((freq.get(l, .0), l) for l in Permutation.CHARS)
        return Permutation(''.join(x for _, x in flist))


    def initialkey(self, ciphertext, langdata):
        cperm = {l : ciphertext.count(l) / len(ciphertext)
                for l in Permutation.CHARS}
        lperm = langdata.ngrams(1)
        return self._freq2perm(cperm) @ ~self._freq2perm(lperm)


    def neighbourhood(self, key, ciphertext, langdata):
        letters = Permutation.CHARS
        for i in range(0, len(letters)):
            for j in range(0, i):
                if letters[i] in ciphertext or letters[j] in ciphertext:
                    yield Permutation.inversion(letters[i], letters[j]) @ key



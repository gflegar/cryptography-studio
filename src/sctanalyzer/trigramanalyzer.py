"""
This module provides the TrigramAnalyzer class that implements the LangData
abstract class.
"""

from filelangdata import FileLangData

class TrigramAnalyzer(FileLangData):
    """
    This class is a concrete implementation of the LangData abstract class.

    It uses trigrams to determine if a given text belongs to the given
    language.
    """
    def quality(self, plaintext):
        freq = {}
        for i in range(0, len(plaintext) - 2):
            trigram = plaintext[i:i+3]
            if trigram in freq:
                freq[trigram] += 1
            else:
                freq[trigram] = 1
        for trigram in freq:
            freq[trigram] /= len(plaintext) - 2
        for trigram, f in self.ngrams(3).items():
            if trigram in freq:
                freq[trigram] -= f
            else:
                freq[trigram] = f
        return sum(map(abs, freq.values()))


"""
This module provides a testing implementation of LangData.
"""

from langdata import LangData

class HrAFreq(LangData):
    """
    A simple testing implementation of LangData for croatian language.
    """
    def quality(self, plaintext):
        return 0.12 - plaintext.count('A') / len(plaintext)


    def ngrams(self, n):
        return {'A' : 0.12} if n == 1 else {}


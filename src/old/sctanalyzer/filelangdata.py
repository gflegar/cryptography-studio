"""
This module provides an extension of LangData class that allows reading the
language data from a JSON file.
"""

import json

from langdata import LangData

class FileLangData(LangData):
    """
    A partial implementation of LangData class that allows reading data from
    JSON files.
    """
    NGRAM_SUFFIX = "graph"

    def __init__(self, filename):
        """
        Initialize a new FileLangData object with data from file _filename_.
        """
        self._ngrams = self._fromJSON(filename)


    def _fromJSON(self, filename):
        """
        Read language data from file _filename_.
        """
        langfile = open(filename, 'r')
        ngrams = json.load(langfile)
        langfile.close()
        return ngrams

    def ngrams(self, n):
        gramname = str(n) + self.NGRAM_SUFFIX
        if gramname in self._ngrams:
            return self._ngrams[gramname]
        else:
            raise ValueError("{}-grams are not listend in this LanguageData"
                    .format(n))


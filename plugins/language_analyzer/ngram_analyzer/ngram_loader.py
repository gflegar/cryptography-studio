""" This module provides a loader class that reads data from language .json
files in the langfiles directory. """


import os
from os import path
import json


class NGramLoader(object):
    """ This class reads the .json files containing frequnecies of ngrams in
    the specified language.

    Args:
        NGRAM_FORMAT: string, name of the n-gram propery in .json object
    """
    NGRAM_FORMAT = "{}graph"

    def __init__(
            self,
            dirname = path.join(path.dirname(__file__), "langfiles")):
        """ Create a new NGramLoader instance.

        Args:
            dirname: directory containing the language files
        """
        self._dirname = dirname

    def load(self, filename):
        """ Load the specified language file.

        Args:
            filename: name of the language file
        """
        with open(path.join(self._dirname, filename)) as fp:
            self._loaded = json.load(fp)

    def get_files(self):
        """ Get available language files.

        Returns:
            List of language file names.
        """
        return os.listdir(self._dirname)

    def get_ngrams(self, n):
        """ Return a dictionary of n-grams and frequnecies read from the
        language file.

        Args:
            n: length of the n-gram

        Returns:
            Dictionart with n-grams as keys and frequnecies as values.
        """
        return self._loaded.get(self.NGRAM_FORMAT.format(n), {})


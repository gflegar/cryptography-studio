import os
from os import path
import json


class NGramLoader(object):
    NGRAM_FORMAT = "{}graph"
    def __init__(
            self,
            dirname = path.join(path.dirname(__file__), "langfiles")):
        self._dirname = dirname

    def load(self, filename):
        with open(path.join(self._dirname, filename)) as fp:
            self._loaded = json.load(fp)

    def get_files(self):
        return os.listdir(self._dirname)

    def get_ngrams(self, n):
        return self._loaded.get(self.NGRAM_FORMAT.format(n), {})


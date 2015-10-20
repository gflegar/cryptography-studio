"""
TODO: Write documentation.
"""

class SCTAnalyzer(object):
    """
    TODO
    """
    def __init__(self, cipher, langdata):
        """
        TODO: Write documentation.
        """
        self._cipher = cipher
        self._ciphertext = None
        self._langdata = langdata
        self._currkey = None
        self._currqual = None
        self._tabulist = None
        self._wrongsols = set()


    def key(self):
        """
        Get current key.
        """
        return self._currkey


    def plaintext(self):
        """
        Get current plaintext.
        """
        return self._cipher.decrypt(self._ciphertext, self._currkey)


    def initialize(self, ciphertext, tabusize):
        """
        TODO
        """
        self._ciphertext = ciphertext
        self._currkey = self._cipher.initialkey(ciphertext)
        self._tabulist = [None] * tabusize
        self._tabulistnext = 0

    def nextiter(self):
        """
        TODO
        """
        if not self._currkey:
            raise RuntimeError("Tabu search not initialized.")
        self._tabulist[self._tabulistnext] = self._currkey
        self._tabulistnext = (self._tabulistnext + 1) % len(self._tabulist)
        self._currqual, self._currkey = min(self._getneighbourhood())
        return self.plaintext()


    def _getneighbourhood(self):
        for key in self._cipher.neighbourhood(
                self._currkey,
                self._ciphertext):
            if key in self._tabulist or key in self._wrongsols:
                continue
            quality = self._langdata.quality(
                        self._cipher.decrypt(self._ciphertext, key))
            yield quality, key


if __name__ == "__main__":
    import doctest
    doctest.testmod()


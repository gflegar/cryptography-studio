"""
This module provides a SCTAnalyzer class that implements a tabu search
heuristic for analyzing general substitution ciphers.
"""

class SCTAnalyzer(object):
    """
    SCTAnalyzer implements a tabu search heuristic that helps break a general
    substitution cipher. The procedure uses provided Cipher and LangData
    implementations that guide the search by providing cipher and language
    specific information.
    """
    def __init__(self, cipher, langdata):
        """
        Create a new SCTAnalyzer object with given Cipher and LangData
        implementations.
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


    def quality(self):
        """
        Get quality of current solution.
        """
        return self._langdata.quality(self.plaintext())


    def plaintext(self):
        """
        Get current plaintext.
        """
        return self._cipher.decrypt(self._ciphertext, self._currkey)


    def setwrong(self):
        """
        Add current solution in wrong solutions.
        """
        self._wrongsols.add(self.plaintext())


    def initialize(self, ciphertext, tabusize):
        """
        Initialize tabu search with given ciphertext and tabu list size.
        """
        self._ciphertext = ciphertext
        self._currkey = self._cipher.initialkey(ciphertext, self._langdata)
        self._tabulist = [None] * tabusize
        self._tabulistnext = 0
        return self.plaintext()


    def nextiter(self):
        """
        Advvance to the next iteration of tabu search.
        """
        if self._currkey is None:
            raise RuntimeError("Tabu search not initialized.")
        if self._tabulist:
            self._tabulist[self._tabulistnext] = self.plaintext()
            self._tabulistnext = (self._tabulistnext + 1) % len(self._tabulist)
        try:
            self._currqual, self._currkey = min(self._getneighbourhood(),
                    key=lambda x: x[0])
        except ValueError:
            raise StopIteration

        return self.plaintext()


    def _getneighbourhood(self):
        """
        Get neighbourhood of current solution provided by the Cipher, with tabu
        and wrong solutions filtered out and with qualities given by LangData.
        """
        for key in self._cipher.neighbourhood(
                self._currkey,
                self._ciphertext,
                self._langdata):
            plaintext = self._cipher.decrypt(self._ciphertext, key)
            if plaintext in self._tabulist or plaintext in self._wrongsols:
                continue
            quality = self._langdata.quality(
                        self._cipher.decrypt(self._ciphertext, key))
            yield quality, key


if __name__ == "__main__":
    import doctest
    doctest.testmod()


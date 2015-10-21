"""
This module provides base class for LangData classes that provide language
specific information used in SCTAnalyzer.
"""

class LangData(object):
    """
    A base class for all classes providing language specific information.
    """
    def quality(self, plaintext):
        """
        Check if given _plaintext_ belongs to this language.

        Returned number should represent the probability that this plaintext is
        in given language (lower number is better).
        """
        raise NotImplementedError


    def ngrams(self, n):
        """
        Get a dictionary of n-grams and their frequencies in the given
        language.
        """
        raise NotImplementedError

if __name__ == "__main__":
    import doctest
    doctest.testmod()


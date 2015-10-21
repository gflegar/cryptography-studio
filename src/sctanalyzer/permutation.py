"""
This module provides a Permutation class that represents permutations of
english alphabet.
"""

class Permutation(object):
    """
    A class representing permutations of letters.
    """

    _CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _ASIZE = len(_CHARS)

    def __init__(self, perm = None):
        """
        Create a new Permutation.

        If _perm_ is `None` construct a identity.

        >>> Permutation()
        Permutation('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        """
        if not perm:
            perm = self._CHARS
        if len(perm) != self._ASIZE:
            raise ValueError('"{}" is too short.'.format(perm))
        self._perm = perm

    def __hash__(self):
        return hash(self._perm)

    def __eq__(self, other):
        """
        Check if two Permutations are equal.

        >>> Permutation() == Permutation()
        True
        """
        return self._perm == other._perm

    def __repr__(self):
        """
        Get a string representation of Permutation.
        """
        return "Permutation('{}')".format(self._perm)


    def _permute(self, c):
        return self._perm[ord(c.upper()) - ord('A')]


    def __call__(self, text):
        """
        Permute a selected item or range of iterms.

        >>> Permutation('BACDEFGHIJKLMNOPQRSTUVWXYZ')('ABC')
        'BAC'
        """
        return ''.join(map(self._permute, text))

    def __matmul__(self, other):
        """
        Compose two permutations.

        >>> p = Permutation('BACDEFGHIJKLMNOPQRSTUVWXYZ')
        >>> p @ p
        Permutation('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        """
        return Permutation(self(other(self._CHARS)))

    @classmethod
    def inversion(cls, a, b):
        """
        Create an inversion with _a_ and _b_ inverted.

        >>> Permutation.inversion('A', 'Z')
        Permutation('ZBCDEFGHIJKLMNOPQRSTUVWXYA')
        """
        a = a.upper()
        b = b.upper()
        def invert(x):
            if x == a:
                return b
            if x == b:
                return a
            return x
        return Permutation(''.join(map(invert, cls._CHARS)))

    @classmethod
    def shift(cls, i):
        """
        Create a shift _i_ places to the left.

        >>> Permutation.shift(5)
        Permutation('FGHIJKLMNOPQRSTUVWXYZABCDE')
        """
        return Permutation(cls._CHARS[i:] + cls._CHARS[:i])

if __name__ == "__main__":
    import doctest
    doctest.testmod()

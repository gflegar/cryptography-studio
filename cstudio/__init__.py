""" The cstudio module implements Cryptography Studio's core functionalities.

It does not provide support for any specific ciphers, language or cipher
analzers. These functionalities are provided by various plugins which are
located in the plugins module.
"""


from cstudio.cryptography_studio import CryptographyStudio


class Error(Exception):
    """ Base for all exceptions thrown by cstudio module.

    All other exceptions that are thrown by cstudio method should extend
    this class.
    """
    pass


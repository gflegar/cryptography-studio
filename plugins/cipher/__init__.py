""" The cipher subpackage provides plugins that are able to encrypt and decrypt
various ciphers.

All plugins in this package should implement the Cipher ABC defined in the
cipher submodule.
"""


from plugins.cipher import cipher


ABC = cipher.Cipher


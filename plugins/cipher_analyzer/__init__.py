""" The cipher alanyzer subpackage provides plugins that analyze various cipher
and help with their decryption.

All plugins in this package should implement the CipherAnalyzer ABC defined in
the cipher_analyzer submodule.
"""


from plugins.cipher_analyzer import cipher_analyzer


ABC = cipher_analyzer.CipherAnalyzer


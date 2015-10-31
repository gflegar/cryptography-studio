""" The language alanyzer subpackage provides plugins that analyze language
properties useful for breaking ciphers.

All plugins in this package should implement the Language ABC defined in
the language submodule.
"""


from plugins.language_analyzer import language_analyzer


ABC = language_analyzer.LanguageAnalyzer


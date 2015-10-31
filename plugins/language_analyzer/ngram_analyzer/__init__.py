""" This package implements the Ngram Analyzer plugin.

It calcualates the n-gram frequencies in the text and compares them with n-gram
frequencies in the selected language. Data about various languages is stored in
the langfiles subdirectory.
"""


from plugins.language_analyzer.ngram_analyzer import ngram_analyzer


MAIN = ngram_analyzer.NGramAnalyzer


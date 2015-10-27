import abc


class CipherAnalyzer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, parent): pass

    @abc.abstractmethod
    def get_widget(self): pass


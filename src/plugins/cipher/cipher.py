import abc


class Cipher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def encrypt(self, plaintext, key): pass

    @abc.abstractmethod
    def decrypt(self, ciphertext, key): pass

    @abc.abstractmethod
    def get_widget(self): pass


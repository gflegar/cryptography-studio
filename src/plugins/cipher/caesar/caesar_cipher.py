from gi.repository import Gtk


from plugins.cipher import cipher


class CaesarCipher(cipher.Cipher):
    def __init__(self, parent):
        self._parent = parent

    def encrypt(self, plaintext, key):
        return plaintext

    def decrypt(self, ciphertext, key):
        return ciphertext

    def get_widget(self):
        return Gtk.Label("Ceasar cipher plugin")

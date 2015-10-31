Cryptography Studio
===================

What is it?
-----------

__Cryptography Studio__ is an application that helps you encrypt and decrypt
messages and break various ciphers (provided by the plugins). It was created as
a helper tool to minimize the amount of hand calculation when solving homeworks
for the course "_Cryptography and Network Security_" at _University of Zagreb_.

### Features:

* encryption and decryption of texts with diferent ciphers
* tools for cryptoanalysis of encrypted texts
* a plugin system that lets you implement (in _Python_) your own ciphers and
  cryptoanalysis tools to extend the abilities of the program -- in fact, every
  implemented cipher is actualy a plugin, the core of the program cannot do
  anything usefull realy :)

What is it not?
---------------

It doesn't break ciphers by itself (yet!) -- it does simple mundane tasks
(like n-gram frequency analysis, encryption and decryption).

List of plugins
---------------

* Encryption/decryption
    * [Simple substitution cipher](
      https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution)
    * [Vigenere's cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
* Cryptoanalysis
    * [Simple substitution cipher](
      https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution)
* Language analysis
    * [N-gram analysis](https://en.wikipedia.org/wiki/N-gram)

Instalation
-----------

### Dependencies

* _Python 3.5_
* _GTK+ 3.16_
* _PyGObject_

On _ArchLinux_ dependencies can be installed by runing:
`pacman -S gtk3 pygobject`

On _Ubuntu_ the following should work (_not tested_, but it doesn't work on
15.04 because the GTK+ version in official repositories is 3.14):
`apt-get install python3 python3-gi gtk+3.0`

On _Windows_ download and install (_also not tested_):

* [python 3.5](https://www.python.org/downloads/)
* [PyGObject with GTK+](http://sourceforge.net/projects/pygobjectwin32/)

### Cryptography Studio installation

Clone the repository or download and unpack the .zip file.

### Run the program

Run `cryptography-studio` located at package's root directory (try running it
with `python3` if that doesn't work).

Screenshots
-----------

![Encrypt/decrypt tab image](
https://raw.githubusercontent.com/gflegar/cryptography-studio/master/screenshots/encrypt_decrypt.png)

![Analyze tab image](
https://raw.githubusercontent.com/gflegar/cryptography-studio/master/screenshots/analyze.png)

The first screenshot shows the Encrypt/Decrypt tab which consists of a text-box
(1) that contains a message to be encrypted and a plugin area (2) where an
encryption/decryption plugin can be loaded (in this case it's the Vigenere's
cipher plugin). Once you click the encrypt button the plaintext in the box is
replaced with the ciphertext. By clicking the decrypt button, ciphertext is
transformed back to plaintext.

The second image shows the Analyze tab used for cryptoanalysis. In this case
there are two text-boxes, one for the original ciphertext (3), and the other
for the (possibly) decrypted plaintext. There are two plugin areas here. The
bottom one (4) contains a cryptoanalysis plugin (in this case the one for
Substitution cipher), and the right one (5) a language anayzer (in this
case the N-gram analyzer).


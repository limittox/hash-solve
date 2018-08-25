from hashlib import md5
from modules.decrypter import Decrypter

# Attack modes
BRUTE_FORCE = 0
WORDLIST = 1

class MD5(object):
    def __init__(self, wordlist=None, rules=None):
        self.wordlist = wordlist
        self.rules = rules

    def encrypt(self, text):
        h = md5()
        h.update(text.encode('utf-8'))
        return h.hexdigest()
    
    def decrypt(self, hash, passSize=None):
        if passSize is None:
            passSize = 8

        if self.wordlist is None and self.rules is None:
            return Decrypter(self, hash, passSize).decrypt_brute(hash)
        elif self.rules is None:
            return Decrypter(self, hash, passSize).decrypt_wordlist(hash, self.wordlist)
        else:
            return Decrypter(self, hash, passSize).decrypt_wordlist_rules(hash, self.wordlist, self.rules)
        
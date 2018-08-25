from modules.iterString import iter_all_strings
# from modules.rules import Rules
from modules.ruleManager import ruleManager
from timeit import default_timer as timer

class Decrypter(object):
    def __init__(self, hashType, hash, passSize):
        self.hashType = hashType
        self.hash = hash
        self.passSize = passSize
    
    def decrypt_brute(self, hash):
        start = timer()
        for i in range(1,self.passSize):
            gen = iter_all_strings(i)
            it = 1
            for s in gen:
                checkStrEncrpt = self.hashType.encrypt(s)
                if hash == checkStrEncrpt:
                    end = timer()
                    print(f'Execution Time: {end-start}')
                    return s
                
                if it == 26**i:
                    break
                it += 1
        return 'FAILED :('

    def decrypt_wordlist(self, hash, wordlist):
        start = timer()
        for s in wordlist:
            # print(s)
            checkStrEncrpt = self.hashType.encrypt(s)
            if hash == checkStrEncrpt:
                end = timer()
                print(f'Execution Time (Decryption): {end-start}')
                return s
        return "FAILED :("
    
    def decrypt_wordlist_rules(self, hash, wordlist, rules):
        start = timer()
        for i, s in enumerate(wordlist):
            if i % 1e6 == 0:
                end = timer()
                print('{} out of {} words tested with {} combinations | Time for {}: {}'.format(i, len(wordlist), i*len(rules), i, (end-start)))
                # print(f'{i} out of {len(wordlist)} words tested with {i*len(rules)} combinations | Time for {i}: {end - start}')
                start = timer()
            # print(s)
            for r in rules:
                checkStr = ruleManager(s, r)
                # checkStr = Rules(s).ruleManager(r)
                # print(checkStr)
                checkStrEncrpt = self.hashType.encrypt(checkStr)
                if hash == checkStrEncrpt:
                    # end = timer()
                    # print(f'Execution Time (Decryption): {end-start}')
                    return s
        return "FAILED :("
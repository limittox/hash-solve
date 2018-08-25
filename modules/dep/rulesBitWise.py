x = 32
LOWER = frozenset('abcdefghijklmnopqrstuvwxyz')
UPPER = frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

LOWER_D = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
    'i': 105,
    'j': 106,
    'k': 107,
    'l': 108,
    'm': 109,
    'n': 110,
    'o': 111,
    'p': 112,
    'q': 113,
    'r': 114,
    's': 115,
    't': 116,
    'u': 117,
    'v': 118,
    'w': 119,
    'x': 120,
    'y': 121,
    'z': 122,
}
UPPER_D = {
    'A': 65,
    'B': 66,
    'C': 67,
    'D': 68,
    'E': 69,
    'F': 70,
    'G': 71,
    'H': 72,
    'I': 73,
    'J': 74,
    'K': 75,
    'L': 76,
    'M': 77,
    'N': 78,
    'O': 79,
    'P': 80,
    'Q': 81,
    'R': 82,
    'S': 83,
    'T': 84,
    'U': 85,
    'V': 86,
    'W': 87,
    'X': 88,
    'Y': 89,
    'Z': 90,
}

class Rules(object):
    def __init__(self, passString):
        self.passString = passString
    
    def ruleManager(self, rule):
        ruleAndFunc = {
            ':': self.nothing(), 
            'l': self.lowercase(), 
            'u': self.uppercase(), 
            'c': self.capitalize(), 
            'C': self.invertCapitalize(),
            't': self.toggleCase()
        }
        
        # modifiedPassString = ruleAndFunc.get(rule)()
        return ruleAndFunc.get(rule)

    def nothing(self):
        return self.passString

#  caps=frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZ')" "'X' in caps

    # def isLower(self, i):
    #     if i in LOWER:
    #         return True
    #     return False

    # def isUpper(self, i):
    #     if i in UPPER:
    #         return True
    #     return False

    def lowercase(self):
        s = ''
        for i in self.passString:
            if i in LOWER:
                s += chr(LOWER_D.get(i) | x)
            else:
                s += i
        return s

    def uppercase(self):
        s = ''
        for i in self.passString:
            if i in UPPER:
                s += chr(UPPER_D.get(i) & ~x)
            else:
                s += i
        return s
    # First letter capital, rest lower case
    def capitalize(self):
        s = ''
        for i in self.passString:
            if i in LOWER and len(s) == 0:
                s += chr(LOWER_D.get(i) & ~x)
            else:
                s += i
        return s

    # First letter lowercase, rest capital
    def invertCapitalize(self):
        s = ''
        for i in self.passString:
            if i in LOWER and len(s) == 0:
                s += chr(LOWER_D.get(i) | x)
            elif i in LOWER:
                s += chr(LOWER_D.get(i) & ~x)
            else:
                s += i

        return s
    
    # Invert case of letters
    def toggleCase(self):
        s = ''

        for i in self.passString:
            if i in LOWER:
                s += chr(LOWER_D.get(i) & ~x)
            elif i in UPPER:
                s += chr(UPPER_D.get(i) | x)
            else:
                s += i
        return s


# print(Rules("Hello").lowercase())
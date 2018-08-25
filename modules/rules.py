class Rules(object):
    def __init__(self, passString):
        self.passString = passString
        # self.rule = rule
    
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
    
    def lowercase(self):
        return self.passString.lower()
    
    def uppercase(self):
        return self.passString.upper()

    # First letter capital, rest lower case
    def capitalize(self):
        return self.passString.capitalize()
        # s = ''
        # for i in self.passString:
        #     if i.islower() and len(s) == 0:
        #         s += i.upper()
        #     else: 
        #         s += i
        # return s

    # First letter lowercase, rest capital
    def invertCapitalize(self):
        return self.passString.capitalize().swapcase()
        # s = ''
        # for val in self.passString:
        #     if val.isalpha() and val.islower() and len(s) == 0:
        #         s += val.upper()
        #     elif val.isalpha() and val.isupper() and len(s) > 0:
        #         s += val.lower()
        #     else:
        #         s += val
        # return s
    
    # Invert case of letters
    def toggleCase(self):
        return self.passString.swapcase()
        # s = ''
        # for i in self.passString:
        #     if i.islower():
        #         s += i.upper()
        #     elif i.isupper():
        #         s += i.lower()
        #     else:
        #         s += i
        # return s
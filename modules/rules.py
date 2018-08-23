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
    
    def lowercase(self):
        return self.passString.lower()
    
    def uppercase(self):
        return self.passString.upper()

    # First letter capital, rest lower case
    def capitalize(self):
        if self.passString.isalpha():
            return self.passString[0].upper() + self.passString[1:].lower()
        return "null"

    # First letter lowercase, rest capital
    def invertCapitalize(self):
        if self.passString.isalpha():
            return self.passString[0].lower() + self.passString[1:].upper()
        return "null"
    
    # Invert case of letters
    def toggleCase(self):
        s = [i for i in self.passString]
        newS = []
        for i in s:
            if i.islower():
                newS.append(i.upper())
            elif i.isupper():
                newS.append(i.lower())
        return ''.join(newS)
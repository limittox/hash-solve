from modules.rules import Rules

def ruleManager(passString, rule):
    ruleAndFunc = {
            ':': nothing(passString), 
            'l': lowercase(passString), 
            'u': uppercase(passString), 
            'c': capitalize(passString), 
            'C': invertCapitalize(passString),
            't': toggleCase(passString)
        }
    return ruleAndFunc.get(rule)

def nothing(passString):
        return passString
    
def lowercase(passString):
    return passString.lower()

def uppercase(passString):
    return passString.upper()

# First letter capital, rest lower case
def capitalize(passString):
    if passString.isalpha():
        return passString[0].upper() + passString[1:].lower()
    return "null"

# First letter lowercase, rest capital
def invertCapitalize(passString):
    if passString.isalpha():
        return passString[0].lower() + passString[1:].upper()
    return "null"

# Invert case of letters
def toggleCase(passString):
    s = [i for i in passString]
    newS = []
    for i in s:
        if i.islower():
            newS.append(i.upper())
        elif i.isupper():
            newS.append(i.lower())
    return ''.join(newS)
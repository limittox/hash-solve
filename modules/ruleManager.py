# from modules.rules import Rules

def ruleManager(passString, rule):
    if rule == ':':
        return nothing(passString)
    if rule == 'l':
        return lowercase(passString)
    if rule == 'u':
        return uppercase(passString)
    if rule == 'c':
        return capitalize(passString)
    if rule == 'C':
        return invertCapitalize(passString)
    if rule == 't':
        return toggleCase(passString)
    

def nothing(passString):
        return passString
    
def lowercase(passString):
    return passString.lower()

def uppercase(passString):
    return passString.upper()

# First letter capital, rest lower case
def capitalize(passString):
    return passString.capitalize()

# First letter lowercase, rest capital
def invertCapitalize(passString):
    return passString.capitalize().swapcase()

# Invert case of letters
def toggleCase(passString):
    return passString.swapcase()
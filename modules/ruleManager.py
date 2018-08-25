# from modules.rules import Rules

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
    return passString.capitalize()

# First letter lowercase, rest capital
def invertCapitalize(passString):
    return passString.capitalize().swapcase()

# Invert case of letters
def toggleCase(passString):
    return passString.swapcase()
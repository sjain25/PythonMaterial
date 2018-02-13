## STRINGS
# Strings in python start & ends with a double quotes
spam = "That is Alice's cat."
print(spam)

## ESCAPE CHARACTERS
# to use single quotes for string, use escape charaters \ for inside string
spam = 'Say hi to Bob\'s mother.'
print(spam)
print("Hello there!\nHow are you?\nI\'m doing fine.")

## RAW STRINGS
# ignores any backslashes in string & type as it is
print(r'That is Carol\'s cat.')

## MULTILINE STRINGS
# written withinn ''' or """
# Any quotes, tabs, or newlines in between the “triple quotes”
# are considered part of the string
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

print('Dear Alice,\nEve\'s cat has been arrested for catnapping, catburglary, and extortion.\n\nSincerely,\nBob')

## INDEXING  SLICING STRINGS
spam = 'Hello world!'
print(spam[0])
print(spam[-1])
print(spam[:5])
print(spam[6:])

## IN NOT IN FUNCTIONS
print('Hello' in 'Hello World') #True
print('HELLO' in 'Hello World') #False - case sensitive
print('' in 'spam') #True

## The upper(), lower(), isupper(), and islower() String Methods
spam = 'Hello world!'
spam = spam.upper()
print(spam)

# using lower in function to ignore case sensitive user inputs:
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# Isupper & Islower
spam = 'Hello world!'
print(spam.islower())
#False
print(spam.isupper())
#False
print('HELLO'.isupper())
#True
print('abc12345'.islower())
#True
print('12345'.islower())
#False
print('12345'.isupper())
#False

## The isX String Methods
#isalpha() - dasjd and not blank
#isalnum() - assd224 & not blank
#isdecimal() - 12.343 & not blank
#isspace() - spaces,newlines,tab & not blank
#istitle() - Ajd Sjdf Akdsd & not blank

print('hello'.isalpha()) #True
print('hello'.isalnum()) #True
print('123'.isdecimal()) #True
print('This Is Title Case 123'.istitle()) #True
print('This Is NOT Title Case Either'.istitle()) #Flase - NOT

# Examples
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

## STARTWITH() & ENDWITH() FUNCTIONS
print('Hello World!'.startswith('Hello'))
print('123abcd34'.endswith('34'))

## THE JOIN() & SPLIT() METHODS
print(','.join(['cats','bats','rats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Shivi.'.split())

#Example
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

## JUSTIFYING TEXT WITH LDUST(), RDUST() & CENTRE()
print('Hello'.rjust(10)) #10 is the space length giveen for string

#print('Hello'.ljust(10, 'World!')) # Throw error, file character must be 1 inlength
# example
print('Hello'.ljust(20, '*'))
print('Hello'.center(20))

# Example in codes
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

## Removing Whitespace with strip(), rstrip(), and lstrip()
spam = '    Hello World     '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) #strip function ignore the sequsnce of character been striped
# ampS = apSm = aSpm etc

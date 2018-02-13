## FINDING PATTERN OF TEXT WITHOUT REGULAR EXPRESSSION
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('281-617-8903 is a phone number.')
print(isPhoneNumber('281-617-8903'))
print('Shivi Jain is a phone number')
print(isPhoneNumber('Shivi Jain'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
    print('Done')


# \d in a regex stands for a digit character—that is, any single numeral 0 to 9
# \d\d\d-\d\d\d-\d\d\d\d - matches 3integer-3integer-4integer or
# \d{3}-\d{3}-\d{4} - more shorter way

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# r is given to pass raw strings which ignores backslashes

## MATCHING REGEX OBJECT
mo = phoneNumRegex.search('My number is 415-555-4242.')
# search method returns none if not found
print('Phone number found: ' + mo.group())
# group method returns actual matched text from searched string

## Examples
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
# '415'
print(mo.group(2))
# '555-4242'
print(mo.group(0))
# '415-555-4242'
print(mo.group())
# '415-555-4242

print(mo.groups())
# 415, 555-4242
areacode, mainNumber = mo.groups()
print(areacode) # 415
print(mainNumber) # 555-4242

## To match paranthesis in sentences
# add a backslash\ before the parathesis
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group())

# Example
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# Bat is the mandatory start check in string followed by either man,mobile,copter or bat
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) #'Batmobile'
print(mo.group(1)) #'mobile'

## Optional Matching with the Question Mark
# ? refers to optional match in a string
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) #Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) #Batwoman

## Matching Zero or More with the Star
# * refers to match zero or more
# the group that precedes the * can occur any number of times in the text
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # Batman
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group()) # Batwowowowoman

## Matching One or More with the Plus
# + matches one or more
# the group preceding a plus must appear at least once
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
#print(mo3.group()) # error - NoneType - object has no attribute 'group'
print(mo3 == None)

## Matching Specific Repetitions with Curly Brackets
# {} brackets include specific quantity to be checked for text
# Only specific quantity is matched
batRegex = re.compile(r'Bat(wo){3}man')
mo1 = batRegex.search('The Adventures of Batwowowoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2 == None)

## Greedy and Nongreedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
# ? refers to nongreedy stuff by choosing shorter length
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group()) # chooses larger number
print(mo2.group()) # chooses smaller number

## The findall() Method
# findall() gives all the matches text in a for of list - no groups
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo1 = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1.group())
print(mo2)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1)

## CHARACTER CLASSES
'''\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the underscore character.
\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S Any character that is not a space, tab, or newline.'''

# Example
# The regular expression \d+\s\w+ will match text that has one or more numeric digits
# (\d+), followed by a whitespace character (\s), followed by one or more
# letter/digit/underscore characters (\w+).
# The findall() method returns all matching strings of the regex pattern in a list.
xmasRegex = re.compile(r'\d+\s\w+')

## Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo1)

# Example of classes:
#[a-zA-Z0-9] #includes every lower upper case letter & digits 0-9
#[0-5.] #includes digit 0-5 & .
#[a-z0-9] #lower case letter & digit 0-9

# Example for negative classes
# ^ this sign negates the classes
# below created class includes everything but lower & upper vowels
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo1 = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo1)

## The Caret and Dollar Sign Characters
# ^ before the character class x indicates that string should start with x
# $ after the character class x indicates string should ennd with x
# example
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello WOrld!')
print(mo1)
print(beginsWithHello.search('He said hello.') == None)

# r'\d$' => string should ends with digit 0-9
# r'^\d+$' => string should start & end with 1 or more digits from 0-9

## The Wildcard Character
# . sign matches any charatcer except new line
atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
# here insated of flat anser will be just lat becasue .at will just
# take a single letter before
print(mo1)

## MATCHING EVRYTHING WITH DOT-STAR
# Remember that the dot character means “any single character except the newline,”
# and the star character means “zero or more of the preceding character.”
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo1 = nameRegex.search('Create Profile. First Name: Shivi. Now print your last name. Last Name: Jain. Now tell your age.')
# Answer will not Create Profile as written before defined class
print(mo1.group())

# To match any and all text in a nongreedy fashion
# use r'<.*?>'

## Matching Newlines with the Dot Character
# Example
noNewlineRegex = re.compile('.*')
mo1 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# answer will only include 1st line because of . symbol
print(mo1)
newlineRegex = re.compile('.*', re.DOTALL)
mo2 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# answer wwill include all line because of re.DOTALL method
print(mo2)

'''
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.'''

## Case-Insensitive Matching
# re.I - ignore case sensitivity
robocop = re.compile(r'robocop', re.I)
mo1 = robocop.search('Robocop is part man, part machine, all cop.').group()
print(mo1)
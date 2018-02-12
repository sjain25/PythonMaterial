## DICTIONARY DATA TYPE
# In dic, indexes can use any data type-char,int unlike list-only integers
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam[12345])

## DIFF BTWN DICTIONARY & LIST
# The order of items matters for determining whether two lists are the same,
# it does not matter in what order the key-value pairs are typed in a dictionary
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
# answer: False
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)
# answer: True

## DICTIONARY CODING
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays: # assigning name name to birthdays dictionary keys
        print(birthdays[name] + ' is birthday of ' + name)# birthday[name] is values of name key
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?') #Entering new data in dictionary
        bday = input()
        birthdays[name] = bday #Assigning value to new key
        print('Birthdays database updated')

## KEYS(), Values(), and Item() Methods
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i) # return tuples for keys & values in dictionary
print(spam.keys())

# converting to list
print(list(spam.keys()))

# seperate key value in for loop
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
# Key: age Value: 42
# Key: color Value: red

## CHECKING WHETHER KEY & VALUE EXIT IN DICTIONARY
spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())
# True
print('Zophie' in spam.values())
# True
print('color' in spam.keys())
# false
print('name' in spam) #shortcut for searching
# True

## get() method
# get method check if value exits else assign a default value
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# 'I am bringing 2 cups.'
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# 'I am bringing 0 eggs.'

picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems['eggs']) + ' eggs.')
# Error : keyError - 'eggs'

## set() method
# general method
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
# set method
spam.setdefault('color', 'black')
print(spam)
spam.setdefault('color', 'white') #since by q1st setdefault method key value has already been set,
# it cant be overwritten with another set method
print(spam)

# Example 2
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)

## Pretty Printing
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

## Using Data Structures to Model Real-World Things
## TIC-TAK-TOE GAME
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
## dictionary is working as a data structure with 9 values:
# so all 9 values should be given while changing code
#theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
#'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
#printBoard(theBoard)

# User input TIC TAK TOE:
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

## NESTED DICTIONARIES & LISTS
# GUEST LIST PROGRAM
allGuests = { 'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

## FANTACY GAME INVENTORY
import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))
displayInventory(stuff)


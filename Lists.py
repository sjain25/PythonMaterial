## LISTS
# open & ends in [] brackets
list = [1, 2, 3]
print(list)
var = ['cats', 'dogs', 'elephants']
print(var)
list2 = ['hello', 3.1415, True, None, 42]
print(list2)

## FETCHING INDIVIDDUAL VALUES FROM LIST
list2 = ['hello', 3.1415, True, None, 42]
print(list2[0])
print(['cat', 'bat', 'rat', 'elephant'][3])
print('Hello ' + list2[0])
print('Hello ' + str(list2[1]))

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[1])
# answer will be 'bat'

print(spam[int(1.0)])
# answer will be 'bat

#print(spam[1.0])
# answer will be
# TypeError: list indices must be integers, not float

# Multiple lists in a list
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
# answer should be ['cat', 'bat']
print(spam[0][1])
# answer will be 'bat'
print(spam[1][4])
# answer will be 50

## Negative INDEXES
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
# answer should be 'elephant'
print(spam[-3])
# answe should be 'bat'
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')
# answer should be - 'The elephant is afraid of the bat.'

## GETTING SUBLISTS WITH SLICES
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
# answer will be ['cat', 'bat', 'rat', 'elephant']
print(spam[1:3])
# answer will be ['bat', 'rat']
print(spam[0:-1])
# answer will be - ['cat', 'bat', 'rat']

## SHORTCUTS
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
# answer should be ['cat', 'bat']
print(spam[1:])
# answer will be ['bat', 'rat', 'elephant']
print(spam[:])
# answer will be ['cat', 'bat', 'rat', 'elephant']

## CHANGING VALUES IN A LIST WITH INDEXES
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)

## LIST CONCATENATION & REPLICATION
print([1, 2, 3] + ['A', 'B', 'C'])
# [1, 2, 3, 'A', 'B', 'C']
print(['X', 'Y', 'Z'] * 3)
# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)
# [1, 2, 3, 'A', 'B', 'C']

## REMOVING VALUES FROM LIST WITH DEL STATEMENT
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
# ['cat', 'bat', 'elephant']
del spam[2]
print(spam)
# ['cat', 'bat']

## WORKING WITH LISTS:
print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
catName5 + ' ' + catName6)

# Instead of multiple lines, user should use while & list:
# Initialising list named catNames
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

## FOR LOOPS WITH LISTS
for i in [0, 1, 2, 3]:
    print(i)

## NOTE
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

## IN & NOT IN OPERATORS
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
# True
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
# False
print('howdy' not in spam)
# False
print('cat' not in spam)
# True

# Example 2
petName = ['bullet','snowy','pooka']
print("Enter a pet name.")
name = input()
if name not in petName:
    print('I do not have a pet name ' + name)
else:
    print(name + ' is my pet.')

## MULTIPLE ASSIGNMENT TRICK
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# instead of multiple lines use below code:
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
# The number of variables and the length of the list must be exactly equal,
# or Python will give you a ValueError:
cat = ['fat', 'orange', 'loud']
# size, color, disposition, name = cat
# ValueError: need more than 3 values to unpack

# Swap with multiple assignment
a, b ='Bob','Alice'
a,b =b,a
print(a)
print(b)


## Augmented assignment statement
# spam += 1     spam = spam + 1
# spam -= 1     spam = spam - 1
# spam *= 1     spam = spam * 1
# spam /= 1     spam = spam / 1
# spam %= 1     spam = spam % 1

## Methods and the index(), append(), insert(), remove(), sort() List Methods

## INDEX METHOD IN LIST: Return the index of value in list
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

print(spam.index('howdy howdy howdy'))
# ValueError: 'howdy howdy howdy' is not in list

# When there are duplicates of the value in the list,
# the index of its first appearance is returned
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

## APPENDING VALUES IN LIST
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
spam.insert(1, 'chicken')
print(spam)
spam.insert(-2, 'elephant')
print(spam)

# Insert, Append functions only works with list
eggs = 'Hello'
eggs.append('World')
# AttributeError: 'str' object has no attribute 'append'
# print(eggs)

bacon = 42
bacon.insert(1, 'world')
# AttributeError: 'int' object has no attribute 'insert'
# print(bacon)

## REMOVING VALUES FROM LIST WITH REMOVE
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

# If the value appears multiple times in the list,
# only the first instance of the value will be removed
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)

## SORT METHOD FOR SORTING LIST
# negative scale to incrreasing positive scale
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

# alphabetically sorting of strings in list
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# reverse sorting
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort(reverse=True)
print(spam)
# Second, you cannot sort lists that have both
# number values and string values in List.
# TypeError: '<' not supported between instances of 'str' and 'int'
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
# print(spam)

# Third, sort() uses “ASCIIbetical order” - A,B,C,a,b,c
# rather than actual alphabetical order for sorting strings
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
# normal alphabetical output
spam.sort(key=str.lower)
print(spam)

## EXERCISE: MAGIC 8 BALL
# System should pick a random ball from 1 to 9,
# and print the messages from that numbered ball.
import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])

## LIST_LIKE FUNCTIONS OF STRINGS
name = 'Zophie'
print(name[0])
# 'Z'
print(name[-2])
# 'i'
print(name[0:4])
# 'Zoph'
print('Zo' in name)
# True
print('z' in name)
# False - Case sensitive
print('p' not in name)
# False
for i in name:
    print('* * * ' + i + ' * * *')
# * * * Z * * *
# * * * o * * *
# * * * p * * *
# * * * h * * *
# * * * i * * *
# * * * e * * *

## MUTABLE & IMMUTABLE
# Strings are immutable
name = 'Zophie a cat'
# name[7] = 'the'
# TypeError: 'str' object does not support item assignment

name = 'Zophie a cat'
# assigning to new string
newName = name[0:7] + 'the' + name[8:12]
print(name)
# 'Zophie a cat'
print(newName)
# 'Zophie the cat

## TUPLES
eggs = ('hello', 99, 0.5, 'World')
print(eggs[0])
print(eggs[0:3])
# Tuples are immutable like strings
# TypeError: 'tuple' object does not support item assignment
# eggs[1] = 99
print(eggs)

## types
print(type(('hello',)))
# tuple - , after the last item in tuple & list are acceptable in python
print(type('hello'))
# string

## CONVERTING TUPLES<LIST<STRINGS
print(tuple(['cat', 'dog', 5]))
# ('cat', 'dog', 5)
print(list(('cat', 'dog', 5)))
# ['cat', 'dog', 5]
print(list('hello'))
# ['h', 'e', 'l', 'l', 'o']

# In list assigning 1 list to another, it assigns reference to new list not the values.
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
# [0, 'Hello!', 2, 3, 4, 5]
print(cheese)
# [0, 'Hello!', 2, 3, 4, 5]

## PASSING REFERENCES
def eggs(someParameter):
    someParameter.append('Hello')
# Even though spam and someParameter contain separate references, they both refer
# to the same list. This is why the append('Hello') method call inside the
# function affects the list even after the function call has returned
spam = [1, 2, 3]
eggs(spam)
print(spam)

## COPY FUNCTION OF LIST- Used to copy values inlist instead of references
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
# answer: ['A', 'B', 'C', 'D']
print(cheese)
# answer: ['A', 42, 'C', 'D']

## PRACTISE PROJECT
spam = []
while True:
    print('Enter the ' + str(len(spam) + 1) + ' item of list:')
    name = input()
    if name == '':
        break
    spam = spam + [name] # list concatenation
print('The items in list are:')
# for name in spam:
print(str(spam))

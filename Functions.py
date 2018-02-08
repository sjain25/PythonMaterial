# defining a function named Hello
def hello(): #() defines arguments for a function and : defines a start of function
    print("Howdy!")
    print("Howdy!!")
    print("Hello there?")

# calling function hello
hello()

## DEFINING FUNCTION
# name is argumnet given in parathesis in a function
# hello(name) is overwriting above create hello() function
def hello(name):
    print("Hello" + name)

hello("Alice")
hello("Bob")
# Pyhthon throw error as value stored in paranthesis is forgotten when the function returns.
#print(name)

## DEFINING FUNCTION WITH RANDOM PACKAGE
# installing random package
import random
# defining get answer function
def getAnswer(answerNumber):
     if answerNumber == 1:
           return 'It is certain'
     elif answerNumber == 2:
           return 'It is decidedly so'
     elif answerNumber == 3:
           return 'Yes'
     elif answerNumber == 4:
           return 'Reply hazy try again'
     elif answerNumber == 5:
           return 'Ask again later'
     elif answerNumber == 6:
           return 'Concentrate and ask again'
     elif answerNumber == 7:
           return 'My reply is no'
     elif answerNumber == 8:
           return 'Outlook not so good'
     elif answerNumber == 9:
           return 'Very doubtful'

# assigning random.randint number with arguments 1 and 9 to variable r
r = random.randint(1,9)
# calling get answer function with argument r
fortune = getAnswer(r)
# printing results
print(fortune)

#shorten version of above 3 lines
print(getAnswer(random.randint(1,9)))

## USAGE OF NONE VALUE
#spam = print("Hello!")
#None == spam

## KEYWORD ARGUMENT IN PRINT
print('Hello')
print('World')

# with end keyword
#print('Hello', end='')
#print('World')
# answer should be HelloWorld

print('cats', 'dogs', 'mice')
# answer should be cats dogs mice

#print('cats', 'dogs', 'mice', sep=',')
# answer should be cats,dogs,mice without space

## LOCAL & GLOBAL SCOPE
'''Parameters and variables that are assigned in a called function are 
said to exist in that functions local scope. Variables that are assigned
 outside all functions are said to exist in the global scope.'''

'''Scopes matter for several reasons:
Code in the global scope cannot use any local variables.
However, a local scope can access global variables.
Code in a functions local scope cannot use variables in any other local scope.
You can use the same name for different variables if they are in different scopes. 
That is, there can be a local variable named spam and a global variable also named spam.'''

#error example
def spam():
    eggs = 31337
spam()
# name error : name 'eggs' is not defined as eggs is local variable &
# cant be used globally.
#print(eggs)

## SCOPE OF VARIBALES EXAMPLE
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

## THE GLOBAL STATEMENT
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
#Because eggs is declared global at the top of spam(),
#when eggs is set to 'spam', this assignment is done to the globally scoped eggs.
#No local eggs variable is created'''

'''There are four rules to tell whether a variable is in a local scope or global scope:
If a variable is being used in the global scope (that is, outside of all functions), 
then it is always a global variable.
If there is a global statement for that variable in a function, it is a global variable.
Otherwise, if the variable is used in an assignment statement in the function, 
it is a local variable.
But if the variable is not used in an assignment statement, it is a global variable.'''

##EXAMPLE
def spam():
    global eggs #this is global
    eggs = 'spam'

def bacon():
    eggs = 'bacon' #this is local

def ham():
    print(eggs) #this is global

eggs = 42 #this is global
spam()
print(eggs)

## EXCEPTION HANDLING
def spam(divideBy):
    return 42/divideBy

print(spam(2))
print(spam(12))
# ZeroDIvisionError will prompt
#print(spam(0))
print(spam(1))

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
# Invalid argument will prompt due to exception case
print(spam(0))
print(spam(1))

## EXERCISE : GUESS A NUMBER
#Output should be
'''I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
17
Your guess is too high.
Take a guess.
16
Good job! You guessed my number in 4 guesses!'''

# PROGRAM
# This is a guess the number game.
import random
r = random.randint(1, 20)
print("I am guessing a number between 1 and 20")

# Ask the player to guess 6 times
# using for loop for i=0 to 6
for guessTaken in range(1,7): # guessTaken is int number between 1 and 7
    print('Take a guess.')
    guess = int(input()) # taking input from user between 1 and 20

    if guess < r:
        print('Your guess is too low')
    elif guess > r:
        print('Your guess is too high')
    else:
        break #this will be the correct number case, thus breaking out of the for loop

if guess == r:
    print('Good Job! You guessed my number in ' + str(guessTaken) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(r))


## EXERCISE 2
# COLLATZ SEQUENCE
def collatz():
    # type: () -> object
    print('Enter a number')
    number = input()
    if number%2 == 0:
        a = number // 2
        print(a)
        return a
    else:
        b = 3*number + 1
        print(b)
        return b

x = collatz()
while x != 1:
    number = collatz()
    print(number)
    x-=1

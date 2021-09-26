#creating a random number generator 
#use python library for random
import random

def guess(x):
    random_number = random.randint(1, x)
    #give guess a number so the range will be positive
    guess = 0

    #loop will continue to request a number till a match 
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        #check if user number is lower than generated number
        if guess < random_number:
            print('Sorry, guess again. Too low')
        #check if user number is greater than generated number
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    #if user number matches generated number skip loop and print
    print(f'Yay, congrats. You have guessed {random_number} correctly')

def computer_guess(x):
    #set range of numbers
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)
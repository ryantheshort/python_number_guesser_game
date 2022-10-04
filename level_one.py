from random import randint


# === LEVEL ONE === 
#     In level one, the computer generates a random number between 1 
# and 10 and the user has 3 guesses to pick the correct number. The 
# computer will tell you if you are too high or too low.

# play = True
# while play == True:
#     player = options(input('Pick a number between 1 and 10: '))

def user():
    number = randint(0,10)
    guesses = 0
    options  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while guesses > 3:
        prompt = input('Pick a number between 1 and 10: ')
        guess = int(prompt)

        if player not in options:
            print('That is not a valid guess. Please try again.')
            continue

        guesses = guesses + 1
        
        if guess == number: # CORRECT ANSWER break HERE
            break
        elif guess < number:
            print('Too low! Try again!') 
        elif guess > number:
            print('Too high! Try again!')

    if guess == number:
        print('Correct!')
    elif guess != number:
        print('Out of guesses! Better luck next time!')



#     computer = options[randint(0, 9)] #10 total options

#     if player == computer: #If player gets it correct
#         print('Correct!')
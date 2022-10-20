from random import randint

# === LEVEL ONE === 
#     In level one, the computer generates a random number between 1 
# and 10 and the user has 3 guesses to pick the correct number. The 
# computer will tell you if you are too high or too low.

# play = True
# while play == True:
#     player = options(input('Pick a number between 1 and 10: '))

def user_play():
    number = randint(1, 10)
    guesses = 0
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    while guesses < 3:
        prompt = input('Guess a number between 1 and 10! ')
        guess = int(prompt)

        if guess not in options:
            print('Please enter a valid number.')
            continue

        guesses = guesses + 1

        if guess == number:
            print('Nice job! You are correct!')
            break
        elif guess < number:
            print('Too low! Try again!')
        elif guess > number:
            print('Too high! Try again!')
        
    while guesses == 3:
        if guess != str(number):
            print('Out of guesses! Try again next time!')
            break

if __name__ == '__main__':
    user_play()

#     computer = options[randint(0, 9)] #10 total options

#     if player == computer: #If player gets it correct
#         print('Correct!')

#==== Revied in class: ======

# from random import randint

# computer = randint(1, 10)

# for count in range(3):
#     player = int(input('Guess a number between 1 and 10. '))
#     if player == computer:
#         print('Correct! The number is', player)
#         break
#     elif count == 2:
#         print()
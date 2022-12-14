from random import randint
import time

# Level Two
# In level two, the game is reversed and the user picks a number and the computer 
# then has 3 guesses to select the correct answer.

prompt = input('Pick a number between 1 and 10 for the computer to guess. ')
number = int(prompt)

guesses = 0

while guesses < 3:
    computer_guess = randint(1, 10)
    print('Computer guesses', computer_guess)

    guesses = guesses + 1
    time.sleep(2)

    if computer_guess == number:
        break
    elif computer_guess < number:
        print('Too low!')
    elif computer_guess > number:
        print('Too high!')

    time.sleep(1)

if computer_guess == number:
    print('The computer has guessed your number!')
elif computer_guess != number:
    print('The computer has been bested!')



#=== Review in class ====

# from random import choice

# player = int(input('Pick a number from 1 to 10: '))
# guesses = [i for i in range(1, 11)]

# for count in range(3):
#     computer = choice(guesses)
#     if player == computer:
#         print('Computer guessed', computer,' Correct.')
#         break
#     else:
#         print('Computer guessed', computer,' Incorrect.')
#         guesses.remove(computer)

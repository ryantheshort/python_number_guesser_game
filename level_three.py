from random import randint
import time
# Level Three
# In level three, the computer's guesses are optimized to refine the range 
# on the guesses based on whether they are too high or too low. Print how many 
# guesses it takes computer before it correctly guesses the number.



def computer_playing():
    prompt = input("Pick a random number from 1 to 100 for the computer to guess. ")
    number = int(prompt)
    guesses = 0
    range_high = 100
    range_low = 1
    playing = True

    while playing == True:
            computer_guess = randint(range_low, range_high)
            print('Computer guesses', computer_guess)

            guesses = guesses + 1

            if computer_guess == number:
                print('The computer took', guesses, 'tries to guess your number!')
                playing = False
                break
            elif computer_guess < number:
                print('Too low!')
                range_low = computer_guess + 1
            elif computer_guess > number:
                print('Too high!')
                range_high = computer_guess - 1

            time.sleep(1)

# computer_playing()
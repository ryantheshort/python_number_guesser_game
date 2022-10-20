from random import randint
import time
# Level Three
# In level three, the computer's guesses are optimized to refine the range 
# on the guesses based on whether they are too high or too low. Print how many 
# guesses it takes computer before it correctly guesses the number.



def comp_play():
    prompt = input('Pick a random number from 1 to 100 for the computer to guess. ')
    number = int(prompt)
    guesses = 0
    range_high = 100
    range_low = 1
    playing = True

    while playing == True:
            comp_guess = randint(range_low, range_high)
            print('Computer guesses', comp_guess)

            guesses = guesses + 1

            if comp_guess == number:
                print('The computer took', guesses, 'tries to guess your number!')
                playing = False
                break
            elif comp_guess < number:
                print('Too low!')
                range_low = comp_guess + 1
            elif comp_guess > number:
                print('Too high!')
                range_high = comp_guess - 1

            time.sleep(1)

if __name__ == '__main__':
    comp_play()

# === Review in class ====

# player = int(input('Pick a number from 1 to 10: '))
# computer = 0
# high = 10
# low = 1
# count = 1

# while computer != player: 
#     count += 1
#     computer = (high + low) // 2  #floored quotient. rounds down to the nearest whole number.
#     if computer > player:
#         high = computer - 1
#     elif computer < computer + 1
#     else:
#         print('Computeer found the number', player,'in',count, 'moves.')
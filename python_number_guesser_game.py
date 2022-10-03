from random import randint

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# === LEVEL ONE === 
#     In level one, the computer generates a random number between 1 
# and 10 and the user has 3 guesses to pick the correct number. The 
# computer will tell you if you are too high or too low.

# play = True
# while play == True:
#     player = options(input('Pick a number between 1 and 10: '))



computer = options[randint(0,10)]
guesses = 3
msg = 'You lose!'
while guesses > 0:
    player = int(input('Pick a number between 1 and 10: '))

    if player not in int:
        print("That is not a valid guess. Please try again.")
        continue
        
    if player == computer: # CORRECT ANSWER HERE
        print('Correct!')
        break
    else:
        print(f'Incorrect. Try again! You have {guesses} remaining.') 
        guesses -= 1
        continue

print(msg)


#     computer = options[randint(0, 9)] #10 total options

#     if player == computer: #If player gets it correct
#         print('Correct!')
from level_one import user_play
from level_three import comp_play
#import level 1 & 3. # from level_one import user    // from level_three import user
# Level Four
# In level four, give the user an option to play against the computer 
# or to think of a number for the computer to guess.

player_choice = int(input('Choose to guess the computer\'s number or pick a number for the computer to guess! Type "1" to guess and "2" to pick. '))

if player_choice == 1:
   user_play()
elif player_choice == 2:
    comp_play()
else:
    print('Please enter a valid response.')
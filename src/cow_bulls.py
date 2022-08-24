# Cows and bulls
# step 0 - import cows_bulls_funcs
# step 0a - initial bull count and cow count variables to 0
# step 0b - print a message explaining the game
# step 1 - prompt the user to enter the length of the secret code
#     verify the users input
# step 2 - generate a random secret code with the number of digits entered by the user
#            - ensure there are no duplicate numbers in the code
# step 3 - Until the number of bulls found equal the length of the code
#     step 4 - Prompt the user to enter a guess
#                - verify the users guess is a valid guess
#                     - guess must be the same length as the code
#                       only contain numbers and no duplicates
#     step 5 - check for the number of cows in the users guess
#     step 6 - check for the number of bulls in the users guess
#     step 7 - report to the user the number of cows and bulls found
# step 8 - once number of bulls found equals the length of the code the player wins
#          display a message reveal the code

from cows_bulls_funcs import *  # step 0

cows_found, bulls_found = 0, 0  # step 0a - initializing the number of cows and bulls found to 0

opening_message()  # step 0b
num_digits_in_code = set_code_length()  # step 1 - Get length of code from user
secret_code = gen_code(num_digits_in_code)  # step 2 - Generate the random secret code

while bulls_found != len(secret_code):  # step 3 - loop until player guesses code
    guess = enter_guess(num_digits_in_code)  # step 4 - Get players guess and ensure its valid
    cows_found = count_cows(secret_code, guess)  # step 5 - find number of cows in guess
    bulls_found = count_bulls(secret_code, guess)  # step 6 - find the number of bulls in guess
    if bulls_found != num_digits_in_code:  # skip report if player has cracked the code
        report_results(cows_found, bulls_found)  # step 7 - tell player how many cows and bulls in their guess

code_is_broken(secret_code)  # step 8 - The player has broken the code

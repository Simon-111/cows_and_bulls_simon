# Cows and Bulls
# Function 0 - print messages to explain the game to the user
# Function 1 - set_code_length - Initializing
#    - print info the user needs
#    - Allow the user to enter the length of the secret code
# Function 1a - validate_setup_input - checks for valid input
#    - Returns True for valid input and False for invalid input
# Function 2 - generate_code - to generate a secret code (function)
#    - Takes the length of the code entered by the user
#    - The code must be digits and cannot have repeated digits
#    - Generate list of nums 0-9
#    - Select a number for the secret code and remove it from the list of nums
#         - Repeat above step the number of times equal to the length entered by the user
#    - Return the secret code
# Function 3 - enter_guess - to take user input (ie their guess)
#    - takes code length as an arg to verify length of guess
#    - prompt user to enter their guess
#    - call validate_guess function to ensure the input is valid
#        - If input is invalid prompt the user to enter a new guess
#        - If input is valid return the users guess
# Function 3a - validate_guess - checks if the users input is valid.
#    - takes the length of the code and the users guess as args
#    - check if all characters are digits with no repeats
#        - if True guess is valid therefore return True
#        - if not true guess is invalid and return False
# Function 4 - count_cows - to determine number of cows (a correct number is guessed but in the wrong position)
#    - Take the code and guess as  arguments
#    - initialize a variable num_cows to 0 that will keep track of the number of cows
#    - for each digit in the guess check if it is in the code.
#        - if the digit is in the code check if it is not in the same position.
#            - if it is in not in the same position add 1 to num_cows
#    - return num_cows which is the total number of digits that are in the code but not in the correct place
# Function 5 - count_bulls - to determine number of bulls in the guess (the correct number in the correct position)
#    - take the code and guess as args
#    - initialize a variable num_bulls to 0 that will keep track of the number of bulls
#    - for each digit in the guess check the digit in the same position in the code
#        - If they are the same number add 1 to the number of bulls
#    - return the number of bulls found (ie. numbers that match value and position with the code
# function 6 - report_results - tell the user the num of cows and bulls in their guess
#    - Takes the number of cows and number of bulls as input
#        - print a message the tells the user the number of cows and bulls in their guess
# function 7 - code_is_broken - display a message when the user wins


def opening_message():
    """Function does not take or return anything
    prints message to explain the game
    """
    print("     ---Welcome to Cows and Bulls---", end='\n\n')
    print("- Try to break the secret code")
    print('- If you guess a number that is in the code but not in the correct position')
    print('  it will be counted as a cow.')
    print('- If you guess a number that is in the code and in the same position')
    print('  it will be counted as a bull.', end='\n\n')


def set_code_length():
    """Function prompts the user to input the length of the code
    they will try to guess. Input must be a digit between 2-9

    Function returns the length of the secret code
    """
    while True:  # loop until user enters valid input
        length_code = input('How many digits do you want in the code (2-9): ')
        if validate_setup_input(length_code):  # func returns True for valid input else returns False
            break
    return length_code


def validate_setup_input(user_input):
    """Function takes the users input for the length of the code
    and verifies that the input is valid.

    Function returns True if the input is an int between 2-9
    otherwise it returns False
    """
    if user_input.isdigit() and int(user_input) in range(2, 10):
        return True
    else:
        print(f'Invalid input: {user_input}, Input must be a number between 2 and 9.')
        return False


def gen_code(code_length):
    """Function takes the length of the code(code_length) as an arg
    Generates a random secret code "code_length" number of digits long
    Code will not repeat any digits

    Function Returns the code
    """
    from random import choice as randomly_select
    nums_for_code = list(range(0, 10))
    code = ''  # initialize empty string to store the code
    for num in range(0, code_length):
        digit = randomly_select(nums_for_code)  # randomly select number from list
        code += str(digit)  # Add number to code
        nums_for_code.remove(digit)  # remove the number from list to prevent duplicates
    return code


def enter_guess(len_code):
    """Function takes the length of the code as an argument
    Prompt the guess the code. Repeat prompt until valid input is entered
    Calls validate_guess_input to ensure input from user is valid

    Return the users guess
    """
    while True:
        user_guess = input('Enter your guess to crack the code: ')
        if validate_guess_input(user_guess, len_code):
            break
    return user_guess


def validate_guess_input(guess_to_check, code_length):
    """Function takes the users guess and the length of the code as inputs
    Check if the guess is digits only, the same length as the code, and
    does ont contain repeated numbers

    If checks are passed function returns True
    otherwise if returns False
    """
    check_guess = False  # assume guess is invalid until proven otherwise
    if len({*guess_to_check}) == code_length and guess_to_check.isdigit():
        check_guess = True
    return check_guess


def count_cows(code_cow, guess_cow):
    """Function takes the secret code and the users guess as args
    For each digit in the guess
        Check if the guess is in the code
            If True find the index of the digit and check it with the digit
            in the same index in the code.
                if the match not a cow
            if they aren't equal add one ot the cow count

    returns the number of cows
    """
    cow_count = 0  # initializing the count of the number of cows to 0
    for num in guess_cow:
        if num in code_cow:
            if guess_cow.index(num) != code_cow.index(num):
                cow_count += 1
    return cow_count


def count_bulls(code_bull, guess_bull):
    """function takes the secret code and the users guess as args
    for each digit in the code
        check if the digit is in the code
            If digit is in the code check if the index for that digit matches
                If they match add 1 to the bull count
    return the number of the bulls
    """
    bull_count = 0  # initialize the count of the number of bulls to 0
    for num in range(0, len(code_bull)):
        if guess_bull[num] == code_bull[num]:
            bull_count += 1
    return bull_count


def report_results(cows_in_guess, bulls_in_guess):
    """Function take the number of cows and the number of bulls as args
    print a message letting the user know how many bulls and cows are in their guess
    """
    print(f'Cows = {cows_in_guess}, Bulls = {bulls_in_guess}')


def code_is_broken(cracked_code):
    """Function prints message when player wins
    """
    print("Congratulations! You've cracked the code!")
    print(f'The secret code was {cracked_code}')

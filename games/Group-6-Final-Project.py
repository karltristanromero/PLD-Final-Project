import random
import os

def main():
    
    while True: #Loop through the menu
        clearScreen()
        # Display Main Menu
        print(f'''\n
            =========================================================================
            |                                 {Bold(Yellow('Lobby'))}                                 |
            |                                                                       | 
            | {Bold(Yellow('Menu:'))}                                                                 |          
            |   1. {Italic('Play Hangman')}                                                     |
            |   2. {Italic('Play Guess the Number')}                                            |
            |   3. {Italic('Exit')}                                                             |
            |   4. {Italic('About the Developers')}                                             |
            =========================================================================
        ''')

        # Prompt the user for an option
        n = input("Pick an option: ")

        # Display General Instructions for Hangman 
        if n == "1":
            clearScreen()
            print(
                f''' 
                =========================================================================
                |                        {Bold(Yellow('WELCOME TO HANGMAN!'))}                            |
                |                                                                       | 
                | Instructions:                                                         |
                |  > Try to guess the word by entering any letter from the alphabet     |
                |  > The player is limited to {Red('5 wrong guesses')}.                          |
                |    After the limit of attempts is reached, the hangman completes and  |
                |    the player {Red('loses')}.                                                  |
                |                                                                       |
                |                              {Bold(Yellow('ENJOY!'))}                                   |
                =========================================================================
                ''')
            print ()
            print (f"Press 1 to {Yellow('START')}")
            print (f"Press 2 to return to {Yellow('MENU')}")

            a = input("")

            if a == "1":
                clearScreen()
                print()
                print(f"{Yellow('GAME START!')}")
                hangman()

            elif a == "2":
                clearScreen()
                continue
        elif n == "2":
            clearScreen()

            # Display General Instructions for Guess the Number

            print( 
                f''' 
                =========================================================================
                |                      {Bold(Yellow('WELCOME TO GUESS THE NUMBER!'))}                     |
                |                                                                       | 
                | Instructions:                                                         |
                |  > Choose a {Red('difficulty')} you want to play.                              |
                |  > Try to guess the random number by entering any number from the     |
                |    given range.                                                       |
                |  > After the limit of attempts is reached, the game completes and     |
                |    the player {Red('loses')}.                                                  |
                |                                                                       |
                |                              {Bold(Yellow('ENJOY!'))}                                   |
                =========================================================================
                '''
                ) 
            print (f"Press 1 to {Yellow('START')}")
            print (f"Press 2 to return to {Yellow('MENU')}")

            a = input("")

            if a == "1":
                clearScreen()
                print()
                print(f"{Yellow('GAME START!')}")
                guessTheNumber()

            elif a == "2":
                clearScreen()
                continue
        
        # Exits the entire program
        elif n == "3":
            clearScreen()
            print ()
            print(f"{Bold(Yellow('I guess that is goodbye! Thank you for playing!'))}")
            break

        # Displays the information about the developers
        elif n == "4":
            clearScreen()
            aboutTheDevs()

# Functions for font-styling
def Red(colorChar): 
        return "\033[91m{}\033[00m".format(colorChar)

def Green(colorChar): 
    return "\033[92m{}\033[00m".format(colorChar)

def Yellow(colorChar): 
    return "\033[93m{}\033[00m".format(colorChar)

def Blue(colorChar): 
    return "\033[94m{}\033[00m".format(colorChar)

def Bold(colorChar): 
    return "\033[01m{}\033[00m".format(colorChar)

def Italic(colorChar): 
    return "\033[03m{}\033[00m".format(colorChar)

# Clear Screen
def clearScreen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for re-trial
def try_again_option(game):
        print(f'''

        Press 1 to {Yellow('Try Again')}
        Press 2 to {Yellow('Exit Game')}
        ''')
        choice = input("")
        if choice == "1":
            clearScreen()
            print(
            f'''
\nStarting a new game...

{Yellow('GAME START!')}
            '''
            )
            game()

        elif choice == "2":
            clearScreen()
            return

# Function for Hangman Game
def hangman():

    # List of words the randomizer will go through
    words = ['python', 'code', 'return', 'loop', 'list', 'tuple', 'class', 'module', 'import', 'functions']

    # Hangman Visual ACKKKK SO CUTE ><
    def hangman_visual(incorrect_guesses):
    
        hangman_status = [
            """
            ------
            |    |
            |
            |
            |
            |
            =======
            """,  # Default

            """
            ------
            |    |
            |    O
            |    |
            |   
            |   
            =======
            """,  # 1 wrong guess

            """
            ------
            |    |
            |    O
            |   /|
            |
            |
            =======
            """,  # 2 wrong guesses

            """
            ------
            |    |
            |    O
            |   /|\\
            |
            |
            =======
            """,  # 3 wrong guesses

            """
            ------
            |    |
            |    O
            |   /|\\
            |   /
            |
            =======
            """,  # 4 wrong guesses

            """
            ------
            |    |
            |    O
            |   /|\\
            |   / \\
            |
            =======
            """   # 5 wrong guesses (End)   
        ]
        
        return hangman_status[min(len(incorrect_guesses), 5)]

    # Game Function
    def hangman_game():
        word_to_guess = random.choice(words)
        guessed_word = ['_'] * len(word_to_guess)
        incorrect_guesses = []
        attempts = 5

        # General UI for Hangman
        while attempts > 0:
            print(hangman_visual(incorrect_guesses))
            print(f"Word: {' '.join(guessed_word)}")
            print("Incorrect guesses:", ', '.join(incorrect_guesses))
            
            # Promp for letter guess
            guess = input(f"{Bold('Enter a letter:')} ").lower()
            
            # Validates if input only has 1 letter
            if len(guess) != 1 or not guess.isalpha():
                clearScreen()
                print(f"\n{Red('Invalid input! Please enter a letter.')}")
                continue

            # Checks for duplicate answers
            if guess in guessed_word or guess in incorrect_guesses:
                clearScreen()
                print(f"\n{Red('Opps, you already guessed that letter.')}")
                continue
            
            # Validates if answer is correct
            if guess in word_to_guess:
                clearScreen()
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        guessed_word[i] = guess
                print(f"\n{Bold(Yellow('Good job!'))} '{guess}' is in the word.")
            else:
                clearScreen()
                incorrect_guesses.append(guess)
                attempts -= 1
                print(f"\n{Red('Yikes!')} '{guess}' is not in the word.")

            # Displays UI if user wins
            if '_' not in guessed_word:
                clearScreen()
                print(hangman_visual(incorrect_guesses))
                print(f"\n{Bold(Yellow('Congrats!'))} You guessed the word '{word_to_guess}'.")
                return try_again_option(hangman)
            
            # Displays UI if user loses
            if attempts == 0:
                print(hangman_visual(incorrect_guesses))
                print(f"\n{Red('Game over!')} The word was '{word_to_guess}'.")
                return try_again_option(hangman)    
    hangman_game()               

# Function for Guess the Number Game
def guessTheNumber():

    # Display General UI
    print(f"\n{Bold("Welcome to the Random Number Guessing Game!")}")

    print(f"\n{Bold('Choose Mode')}")
    print("1. Easy (5 attempts)")
    print("2. Difficult (7 attempts)")
    print("3. Impossible (5 attempts)")


    # Get mode
    while True:

        # Validates if input is appropriate
        try:
            mode = int(input(f"\nEnter the mode number ({Yellow('1, 2, or 3')}):"))
            if mode in [1, 2, 3]:
                break
            else:
                print(f"\n{Red('Invalid mode. Please enter 1, 2, or 3.')}")
        except ValueError:
            print(f"\n{Red('Invalid input. Please enter a valid number.')}")

    # Generate UI for chosen game mode
    if mode == 1:
        clearScreen()
        secret_number = random.randint(1, 100)
        attempts_left = 5
        print(f"\nYou selected {Yellow('Easy mode')}. Guess a number between {Yellow('1 and 100.')}\n")
    elif mode == 2:
        clearScreen()
        secret_number = random.randint(1, 1000)
        attempts_left = 7
        print(f"You selected {Yellow('Difficult mode')}. Guess a number between {Yellow('1 and 1000.')}\n")
    else:
        clearScreen()
        secret_number = random.randint(1, 10000)
        attempts_left = 10
        print(f"You selected {Yellow('Impossible mode')}. Guess a number between {Yellow('1 and 10000.')}\n")

    # Guessing loop
    while attempts_left > 0:
        try:
            print(f"Attempts left: {Red(attempts_left)}")
            guess = int(input("Enter your guess: "))
            attempts_left -= 1
            if guess < secret_number:
                print("\nToo low! Try again.")
            elif guess > secret_number:
                print("\nToo high! Try again.")
            else:
                clearScreen()
                # Display UI if the user wins
                print(f"\n{Bold(Yellow('Congratulations!'))} You've guessed the number {secret_number}!")
                try_again_option(guessTheNumber)
                break
        except ValueError:
            print(f"\n{Red('Please enter a valid number.')}\n")

    # Display UI if user loses
    if attempts_left == 0:
        clearScreen()
        print(f"\n{Red('Game Over!')} You've run out of attempts.")
        print(f"The secret number was {secret_number}.")
        try_again_option(guessTheNumber)

# Function for displaying Developers' Information
def aboutTheDevs():
    print(f""" 
          
            =========================================================================
            |                 HELLO! WE ARE THE {Yellow('GROUP 6')} of {Yellow('BSCpE 1-6')} !              |
            |                                                                       |
            |   Good day! This program is the final project for {Blue('CMPE 102')}  -         |
            | {Blue('Programming, Logic, and Design (PLD)')}, handled by Engr. Jan Ruelle     |                 
            | Teña, in the first semester of school year 2024-2025.                 |
            |                                                                       |   
            |                                                                       |
            |   The task given to us was create games, namely: '{Blue('Menu')}', and          |
            | '{Blue('Guess the Number')}.'                                                   |
            |                                                                       |
            | The members of this group are as follows:                             |
            |                                                                       |                                      
            |     Members:                                                          |
            |      > {Yellow('Comia, Mark Lester')} - coded guessTheNumber                      |
            |      > {Yellow('Concepcion, Jacey Erin')} - coded hangman                         |            
            |      > {Yellow('Romero, Karl Tristan')} -  coded the Menu                         |
            |      > {Yellow('Salinas, Nykesha')} - coded hangman                               |
            |                                                                       |
            =========================================================================
          
          """)
    
    # Prompts user to go back to Main Menu
    aboutDevsChoice = input("Click Enter to go back to Main Menu: ")
    if aboutDevsChoice == "":
        return
    
if __name__ == "__main__":
    main()

import random

# List of words the randomizer will go through
words = ['phyton', 'code', 'return', 'loop', 'list', 'tuple', 'class', 'module', 'import', 'functions']

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

    while attempts > 0:
        print(hangman_visual(incorrect_guesses))
        print(f"Word: {' '.join(guessed_word)}")
        print("Incorrect guesses:", ', '.join(incorrect_guesses))
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a letter.")
            continue
        
        if guess in guessed_word or guess in incorrect_guesses:
            print("Opps, you already guessed that letter.")
            continue
        
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
            print(f"\nGood job! '{guess}' is in the word.")
        else:
            incorrect_guesses.append(guess)
            attempts -= 1
            print(f"\nYikes! '{guess}' is not in the word.")

        if '_' not in guessed_word:
            print(hangman_visual(incorrect_guesses))
            print(f"\nCongrats! You guessed the word '{word_to_guess}'.")
            return try_again_option()
        
        if attempts == 0:
            print(hangman_visual(incorrect_guesses))
            print(f"\nGame over! The word was '{word_to_guess}'.")
            return try_again_option()
            
            
# Giving them the option na mag-try ulit
def try_again_option():
    print('''

    Press 1 to Try Again
    Press 2 to Exit Game
    ''')
    choice = input("")
    if choice == "1":
        print(
        '''
      Starting a new game...

      GAME START!
        '''
        )
        hangman_game()

    elif choice == "2":
        return
    

# Display Menu

while True:

    # Display Menu
    print ()
    print ("Menu:")
    print ("1. Hangman")
    print ("2. Guess The Number")
    print ("3. Exit")
    print ("4. Others")

 # Prompt the user for an option
    print ()
    n = input("Pick an option: ")

 # Display General Instructions
    if n == "1":
        print( 
        ''' 
        =========================================================================
        | WELCOME TO HANGMAN!                                                   |
        |                                                                       | 
        | Instructions:                                                         |
        |  > Try to guess the word by entering any letter from the alphabet     |
        |  > The player is limited to 5 wrong guesses.                          |
        |    After the limit of attempts is reached, the hangman completes and  |
        |    the player loses.                                                  |
        |                                                                       |
        | ENJOY!                                                                |
        =========================================================================
        '''
	    ) 
        print ()
        print ("Press 1 to START")
        print ("Press 2 to return to MENU")

        a = input("")

        if a == "1":
            print()
            print("GAME START!")
            hangman_game()

        elif a == "2":
            continue
    
    if n == "3":
        print ()
        print("Goodbye!")
        break

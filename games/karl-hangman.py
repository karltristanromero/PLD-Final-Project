
def hangmanMain():
    # Choose a random word
    lowerWord = randomizer()
    # Create UI for the word
    underscore(lowerWord)
    print(lowerWord)

    # Make lowerword into a list
    lowerList = list(lowerWord)

    correctLetters = [] # Store the value 
    chances = 5

    while True:
        
        if chances > 0:
            guessLetters = input("\nWhat is your letter guess? ").lower()

            if guessLetters.isalpha() == True:
                if len(guessLetters) == 1:
                    if guessLetters in correctLetters:
                        print(f"You already guessed the letter '{guessLetters}'. Try a different one!")
                        continue
                        
                    correctLetters.append(guessLetters)
                
                    if set(correctLetters) == set(lowerList):
                        print(f"\nYou win! The word is '{lowerWord.capitalize()}'")
                        break

                    else:
                        if chances > 0:
                            for char in guessLetters:
                                if char not in lowerList:
                                    chances -= 1
                                    if chances > 0:
                                        print(f"Letter {guessLetters} is not included! Try Again!")
                                        print("\n",f"You only have {chances} chances left! Be careful!")

                            print("Letters: ", end="")       
                            underscoreGuess(lowerWord, correctLetters)
                            print(hangmanPics([6-1]))         
                else:
                    print("Enter single letter only!") 
            else:
                print("Please enter English alphabets only!")
        else:
            print(f"\nSorry but you failed because your chances now are {chances}. The word was '{lowerWord.capitalize()}'\n")
            break
           

# UI for instruction
def underscore(word) -> str:

    print("Guess the word: ")
    for i in range(len(word)):
        print("_", end="  ")
    print("\n")


# Chooses a random word
def randomizer()-> str:
    import random
    
    # Food list
    food = ["Apple", "Bread", "Rice", "Milk", "Egg", "Fish", "Meat", "Cheese", "Sugar", "Water"]

    # Country list
    countries = ["USA", "Canada", "China", "India", "Japan", "Brazil", "France", "Germany", "Italy", "Australia"]

    # Animal list
    animals = ["Dog", "Cat", "Cow", "Horse", "Lion", "Tiger", "Fish", "Bird", "Snake", "Elephant"]

    while True:
        categoryChoice = input("""\nChoose a category you want to guess:     
                                        
        a. Food
        b. Country
        c. Animals                          
                                
Type the letter you have chosen: """)
        
        if categoryChoice.lower() == 'a':
            wordPool = food
        elif categoryChoice.lower() == 'b':
            wordPool = countries
        elif categoryChoice.lower() == 'c':
            wordPool = animals
        else:
            print("Just choose between a, b, and c!")
            continue


        randomWord = random.choice(wordPool)
        lowerCase = randomWord.lower()
        return lowerCase


# Prints underscore/letter based on correctness of guess
def underscoreGuess(word: str, correctGuess: list) -> str:
    for letter in word:
        if letter in correctGuess:
            print("", letter.upper(), "" , end="")
        else:
            print(" _ ", end="")

def hangmanPics():
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return HANGMANPICS
    





hangmanMain()

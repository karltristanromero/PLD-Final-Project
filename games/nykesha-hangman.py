import random

print ("Welcome to Hangman!")

def play_hangman():
    word_list = ["COMPUTER", "ENGINEERING", "PYTHON", "PROGRAMMING", "FRESHMAN"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set(chr(i) for i in range(ord('A'), ord('Z') + 1))
    used_letters = set()
    lives = 6
 
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

    while len(word_letters) > 0 and lives > 0:
        print(HANGMANPICS[6 - lives])
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Guess the word: ", " ".join(word_list))

        print("You have used these letters: ", " ".join(used_letters))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct, you guessed a letter!")

            else:
                lives -= 1
                print("Uh oh, letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(HANGMANPICS[6])
        print("He died :( The word was", word)
    else:
        print("You guessed the word,", word, "!", "You saved the man :)")

play_hangman()

import random
from words_for_hangman import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):

    completion = []
    for i in range(len(word)):
        completion.append("_")
  
    guessed = False
    guessed_letters = []
    tries = 6
    print("HANGMAN")
    print(display_hangman(tries))
    print(completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Already guessed this letter. Enter another letter: ")
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else :
                guessed_letters.append(guess)
                for i in range(len(word)):
                    if list(word)[i] == guess:
                        x = i
                        completion[x] = guess
                if completion == list(word):
                    guessed = True
        else:
            print("Not valid guess, enter a letter.")
        print("You have " + str(tries) + " tries left. \n")
        print(display_hangman(tries))
        print(completion)
        print ("\n")
    if guessed:
        print("Congrats, you guessed the word!")
    else:
        print("You ran out of tries. The word was "+ word +".\n")
    

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[6-tries]
def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N): ").upper() == "Y":
        word = get_word()
        play(word)
if __name__ == "__main__":
    main()



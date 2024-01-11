# Note: tutorial followed from YT video by kite https://www.youtube.com/watch?v=m4nEnsavl6w 
import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6 
    print("Let's Play Taylor Swift Themed Hangman!!")
    print(hangman_display(tries)) 
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter. ").upper()

        # User guesses a valid letter
        if len(guess) == 1 and guess.isalpha(): 
            # Check if user has already guessed the letter
            if guess in guessed_letters:
                print("You already guessed the letter "+ guess + ", please guess again.")
            else:
                # Valid and new guess added to list of guessed letters
                guessed_letters.append(guess)

                if guess not in word: 
                    # Incorect guess
                    tries -= 1
                    print("Aw man, " + guess + " is not in the word.")
                else:
                    # Correct guess
                    print("Booyah! "+ guess + " is in the word.")

                    # NEW From the YT video https://www.youtube.com/watch?v=m4nEnsavl6w 
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for indes in indices:
                        word_as_list[indes] = guess
                    word_completion = "".join(word_as_list)
                    # Check if completed word
                    if "_" not in word_completion:
                        guessed = True

        # User has an invalid guess
        else: 
            print("Not a valid guess.")
        
        # Printouts to start the next turn 
        print(hangman_display(tries))
        print(word_completion)
        print("\n")

    if guessed: 
        print("Congrats! You guessed the word! You win :)")
    else:
        print("Sorry :( you ran out of guesses. " + word + " was the word. Better luck next time.")


def hangman_display(tries):
    stages = [  """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |   
                    |    / \\
                    |
                    ---
                """,
                """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |   
                    |    /
                    |
                    ---
                """,
                """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |
                    |
                    ---
                """,
                """
                    -------
                    |     |
                    |     O
                    |    \\|
                    |     |
                    |
                    |
                    ---
                """,
                """
                    -------
                    |     |
                    |     O
                    |     |
                    |     |
                    |
                    |
                    ---
                """,
                """
                    -------
                    |     |
                    |     O
                    |
                    |
                    |
                    |
                    ---
                """,
                """
                    -------
                    |     |
                    |
                    |
                    |
                    |
                    |
                    ---
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)

    # Some code to make it possible to play again
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
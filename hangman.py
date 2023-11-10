import os

os.system('clear')

# 1. loop max turn counts (6)
# 2. get guess (a letter) from a player
# 3. check if it guess (letter) is inside a secret word
# 4. if not, increase # of wrong counts
# 5. print correct letter
# 6. if all correct, break out of loop

# the secret work the player is trying to guess
secretWord = "CBTNuggets"

# letters guessed; initialize this variable
lettersGuessed = ""

# the number of turns before the player loses
failureCount = 6

# loop until the player has made too many failed attempt
# break loop if they succeed instead
while failureCount > 0:
    
    # Get a guess from the player
    guess = input("Guess a letter: ")
        
    if guess in secretWord:
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Incorrect! There are no {guess} in the secret word. {failureCount} turn(s) left.")

    # Maintain a lis tof all letters guessed
    lettersGuessed = lettersGuessed + guess
    
    # Initialize the number of wrong letters to 0
    wrongLetterCount = 0

    # Go through each letter in the secretWord and compare the letters the player has guessed
    for letter in secretWord:
        if letter in lettersGuessed:
            # Print letters the player has guessed
            print(f"{letter}", end="")
        else:
            # Print an underscore in the place where a letter has not been guessed
            # Count the number of wrong letters
            print("_", end="")
            
            # when wrongLetterCount increases, then the next "if" will not run
            wrongLetterCount += 1
    print("")
    
    # If there were no wrong letters, then the player has won! Break out of the while loop
    if wrongLetterCount == 0:
        print(f"Congratulation! The secret work was: {secretWord}. You won!")
        break

else:
    print("Sorry, you didn't win this time.  Try again!")
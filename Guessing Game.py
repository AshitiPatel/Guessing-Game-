import random #This imports the random module from the standard library
print("These are some words that you probably won't beleive exist") # Prints a string
print(' The words are Bumfuzzle, Cattywampus, Gardyloo, Taradiddle, Pandiculation, Widdershins, Collywobbles, Gubbins, Abibliophobia and Bumbershoot')

words = (['Bumfuzzle', 'Cattywampus', 'Gardyloo', 'Taradiddle', 'Pandiculation', 'Widdershins', 'Collywobbles', 'Gubbins', 'Abibliophobia', 'Bumbershoot']) # List of words that will be picked at random
secret_word = random.choice(words) # Randomly chooses a word
guess = "" # The user's guess will be stored in this variable
guess_count = 0 # Counts how many guesses a user has left
guess_limit = 3 # Limit for the guesses a user has
out_of_guesses = False # Boolean value that states whether the user is out of guesses or not

# These are the clues that will be given to the user to guess the word
if secret_word == 'Bumfuzzle':
     print('Clue: This word means confuse')
elif secret_word == 'Cattywampus':
     print('Clue: This word means destructive')
elif secret_word == 'Gardyloo':
     print('Clue: This word means beware')
elif secret_word == 'Taradiddle':
     print('Clue: This word means a lie')
elif secret_word == 'Pandiculation':
     print('Clue: This word means yawning')
elif secret_word == 'Widdershins':
     print('Clue: This word means counter-clockwise')
elif secret_word == 'Collywobbles':
     print('Clue: This word means an upset stomach')
elif secret_word == 'Gubbins':
     print('Clue: This word means any bits and pieces that are now welcomed to carry')
elif secret_word == 'Abibliophobia':
     print('Clue: This word means the fear of running out of reading material')
elif secret_word == 'Bumbershoot':
     print('Clue: This word means an umbrella')

while guess != secret_word and not(out_of_guesses): # While CURRENTLY THE GUESS of the user is not = to the secret word and out_of_guesses is not True
     if guess_count < guess_limit:
          guess = input("Enter a guess, Make sure that the first letter of the word is in UPPERCASE: ")
          guess_count += 1 #Increases the guess count by 1 
     else:
          out_of_guesses = True

if out_of_guesses: # Output after the user finds out the secret word or didn't 
     print("You Lose! The secret word was" + words)
else:
     print("You Win!")
import pip._vendor.requests as requests
import json
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


random_word = requests.get("https://random-word-api.herokuapp.com/word")

print(random_word.status_code)
print(random_word.text)
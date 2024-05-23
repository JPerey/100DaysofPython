import pip._vendor.requests as requests
import json
#Step 1 


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

def run_game():
    random_word_unfiltered = requests.get("https://random-word-api.herokuapp.com/word")
    random_word_filtered = random_word_unfiltered.text.replace("[","").replace('"',"").replace("]","")
    print(f"random word: {random_word_filtered}")
    player_lives = 3
    word_len = len(random_word_filtered)
    word_list = list(random_word_filtered)
    word_bank = word_len
    hidden_list = []
    for letter in range(word_len):
        hidden_list.append("_")
    print(f"word: {hidden_list}")

    while player_lives > 0:
        player_letter = input("Please guess a letter: ")
        upper_player_letter = player_letter.upper()
        wrong_guess = True
        for i, letter in enumerate(word_list):
            if upper_player_letter == letter.upper():
                hidden_list[i] = upper_player_letter
                wrong_guess = False
                word_bank -= 1
                print(f"word: {hidden_list}")
        if wrong_guess == True:
            player_lives -= 1
            print("Y O U R  G U E S S  W A S  W R O N G. L O S T  A  L I F E.")
            print(f"L I V E S  L E F T: {player_lives}")
        if player_lives == 0:
            print(f" W O R D: {random_word_filtered} || G A M E O V E R.")
        elif word_bank == 0:
                print("C O N G R A T U L A T I O N S ! Y O U  W O N !")
                break
        
            


game_on = True
while (game_on == True):
    player_response = input("Do you want to play Hangman? Y or N")
    upper_player_response = player_response.upper()
    if upper_player_response == "Y":
        run_game()

    else:
        print("G O O D B Y E")
        game_on = False
import random
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
cpu_choice = random.randint(1,100)
print(f"psst, the number is {cpu_choice}")
difficulty = input("What difficulty mode would you want? 'easy' (10 attempts) or 'hard' (5 attempt): 'easy' or 'hard ").lower()
if difficulty == "easy":
    lives = 10
else:
    lives = 5

def play_game ( cpu_choice, lives):
    game_on = True
    while game_on == True:
        print(f"you have {lives} live(s) left")
        player_choice = int(input("please input a number between 1 and 100: "))
        if player_choice == cpu_choice:
            print(f"{player_choice} was the correct number! Congratulations!")
            game_on = False
        elif player_choice > cpu_choice:
            print("Too high")
            lives -= 1
        elif player_choice < cpu_choice:
            print("Too low")
            lives -= 1
        
        if lives == 0:
            print(f"You Lost! The correct number was {cpu_choice}. Better luck next time!")
            game_on = False

            
play_game(cpu_choice, lives)
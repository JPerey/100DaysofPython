from question_bank import Question_Bank
game_process = True
score = 0

question_bank = Question_Bank()
print("Welcome to the Quiz Game")

while game_process == True:
    player_start = input("Would you like to do a 10 question quiz? 'yes' or 'no': ")

    if player_start == "yes":
        question_bank.Get_Quiz()
    else:
        game_process = False
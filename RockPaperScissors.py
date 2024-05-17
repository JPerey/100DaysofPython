import random

player_choice = int(input("what do you choose? type 0 for rock, 1 for paper, or 2 for scissors."))

print(f"player has chosen {player_choice}")
rps_list = ["rock", "paper", "scissors"]
npc_choice = random.randint(0,2)
player_result = rps_list[player_choice]
npc_result = rps_list[npc_choice]

if player_choice == npc_choice:
    both_choice = rps_list[player_choice]
    print(f"tie game. player and npc picked {both_choice}")
elif player_choice == 0 and npc_choice == 1:
    print(f"npc wins. player: {player_result} || npc: {npc_result}")
elif player_choice == 0 and npc_choice == 2:
    print(f"player wins. player: {player_result} || npc: {npc_result}")
elif player_choice == 1 and npc_choice == 0:
    print(f"player wins. player: {player_result} || npc: {npc_result}")
elif player_choice == 1 and npc_choice == 2:
    print(f"npc wins. player: {player_result} || npc: {npc_result}")
elif player_choice == 2 and npc_choice == 0:
    print(f"npc wins. player: {player_result} || npc: {npc_result}")
elif player_choice == 2 and npc_choice == 1:
    print(f"player wins. player: {player_result} || npc: {npc_result}")
else:
    print("somehow wrong number detected")


import os

print("Welcome to the silent auction.")
amount_of_bidders = int(input("How many bidders will be bidding?"))
bidders_list = []
highest_bid = {
    "name": "na",
    "bid": 0,
}

for bidder in range(amount_of_bidders):
    person = input("What is your name?: ")
    person_bid = int(input("What is your bid?: "))
    os.system('clear')
    person_entry = {"person": person,
                    "person_bid": person_bid,
                    }
    bidders_list.append(person_entry)
    if bidders_list[bidder]["person_bid"] > highest_bid["bid"]:
        highest_bid["name"] = person
        highest_bid["bid"] = bidders_list[bidder]["person_bid"]

print("The highest bid was made by " + highest_bid["name"] + " with a bid of " + str(highest_bid["bid"]))


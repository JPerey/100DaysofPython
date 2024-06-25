MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

program_stop = False

def report_resources():
    for item in resources:
        print(f"{item}: {resources[item]}")

def check_cash_input(user_choice_start):
    user_quarters = int(input("how many quarters: "))
    user_dimes = int(input("How many dimes: "))
    user_nickels = int(input("How many nickels: "))
    user_pennies = int(input("How many pennies: "))

    total = (float(user_quarters) * 0.25) + (float(user_dimes) * 0.1) + (float(user_nickels) * 0.05) + (float(user_pennies) * 0.01)

    if user_choice_start == "espresso":
        if total < MENU["espresso"]["cost"]:
            print("Insufficient funds. Money refunded.")
            return False
        elif total > MENU["espresso"]["cost"]:
            change = total - MENU["espresso"]["cost"]
            print(f"Payment accepted. Here is your change - ${change}")
            return True
        else: 
            print(f"Payment accepted.")
            return True
    elif user_choice_start == "latte":
        if total < MENU["latte"]["cost"]:
            print("Insufficient funds. Money refunded.")
            return False
        elif total > MENU["latte"]["cost"]:
            change = total - MENU["espresso"]["cost"]
            print(f"Payment accepted. Here is your change - ${change}")
            return True
        else:
            print(f"Payment accepted.")
            return True
    elif user_choice_start == "cappuccino":
        if total < MENU["cappuccino"]["cost"]:
            print("Insufficient funds. Money refunded.")
            return False
        elif total > MENU["espresso"]["cost"]:
            change = total - MENU["cappuccino"]["cost"]
            print(f"Payment accepted. Here is your change - ${change}")
            return True
        else:
            print(f"Payment accepted.")
            return True

def create_drink(user_choice_start):

    if user_choice_start == "espresso":
        if resources["water"] - MENU["espresso"]["ingredients"]["water"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        elif resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        else:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["water"] - MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your espresso!")
    elif user_choice_start == "latte":
        if resources["water"] - MENU["latte"]["ingredients"]["water"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        elif resources["coffee"] - MENU["latte"]["ingredients"]["coffee"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        elif resources["milk"] - MENU["latte"]["ingredients"]["milk"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        else:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["water"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["water"] - MENU["latte"]["ingredients"]["milk"]
            print("Here is your latte!")
    elif user_choice_start == "cappuccino":
        if resources["water"] - MENU["cappuccino"]["ingredients"]["water"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        elif resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        elif resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"] < 0:
            print("Insufficient resources. Refill Coffee Machine. Money Refunded.")
        else:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["water"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["water"] - MENU["cappuccino"]["ingredients"]["milk"]
            print("Here is your cappuccino!")


while program_stop == False:
    user_choice_start = input("What would you like - espresso, latte, cappuccino, exit, or report?: ").lower()

    if user_choice_start == "report":
        report_resources()
    elif user_choice_start == "exit":
        print("GoodBye!")
        program_stop = True
    elif user_choice_start == "espresso":
        cash_input = check_cash_input(user_choice_start)
        if cash_input == True:
            create_drink(user_choice_start)
    elif user_choice_start == "latte":
        cash_input = check_cash_input(user_choice_start)
        if cash_input == True:
            create_drink(user_choice_start)
    elif user_choice_start == "cappuccino":
        cash_input = check_cash_input(user_choice_start)
        if cash_input == True:
            create_drink(user_choice_start)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_running = True
menu = Menu()
maker = CoffeeMaker()
money_machine = MoneyMachine()
while coffee_running == True:
    print("Hello, I'm your coffee machine! Please input one of the following commands:")
    print("'items' - view menu list \n'latte - order a latte \n'cappuccino - order a cappuccino \n'espresso' - order an espresso")
    print("'report' - show current resources \n'money' - print current money \n'exit' - turn off coffee machine")

    user_choice = input("What would you like to do: ").lower()

    if user_choice == "exit":
        coffee_running = False
    elif user_choice == "report":
        maker.report()
    elif user_choice == "money":
        money_machine.report()
    elif user_choice == "items":
        print(menu.get_items())
    elif user_choice =="cappuccino":
        prospect_drink = menu.find_drink("cappuccino")
        print(dir(prospect_drink))
        print(vars(prospect_drink))
        payment_check = money_machine.make_payment(menu.menu[2].cost)
        if payment_check == True:
            ingredients_check = maker.is_resource_sufficient(prospect_drink)
            if ingredients_check == True:
                maker.make_coffee(prospect_drink)
    elif user_choice =="latte":
        prospect_drink = menu.find_drink("latte")
        print(dir(prospect_drink))
        print(vars(prospect_drink))
        payment_check = money_machine.make_payment(menu.menu[0].cost)
        if payment_check == True:
            ingredients_check = maker.is_resource_sufficient(prospect_drink)
            if ingredients_check == True:
                maker.make_coffee(prospect_drink)
    elif user_choice =="espresso":
        prospect_drink = menu.find_drink("espresso")
        print(dir(prospect_drink))
        print(vars(prospect_drink))
        payment_check = money_machine.make_payment(menu.menu[1].cost)
        if payment_check == True:
            ingredients_check = maker.is_resource_sufficient(prospect_drink)
            if ingredients_check == True:
                maker.make_coffee(prospect_drink)
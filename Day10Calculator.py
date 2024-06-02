def add_nums(num1,num2):
    num_sums = num1 + num2
    return num_sums

def minus_nums(num1,num2):
    num_diffs = num1 - num2
    return num_diffs

def mul_nums(num1,num2):
    num_prods = num1 * num2
    return num_prods

def div_nums(num1,num2):
    num_quots = num1 + num2
    return num_quots

print("Welcome to the awesome calc app!")
user_choice = input("would you like to do a calculation: y or n ").lower()

while user_choice == "y":
    calc_choice = input("Please choose an option with the following options, + - * / : ")
    repeat_calc = "y"
    if calc_choice == "+":
        iter = 0
        while repeat_calc == "y":
            if iter > 0:
                add_num1 = num_sums
            else:
                add_num1 = int(input("What is the first number: "))
            add_num2 = int(input("What is the second number: "))
            num_sums = add_nums(add_num1, add_num2)
            print(f"result: {num_sums}")
            repeat_calc = input("Would you like to reuse the result, and find another sum: y or n").lower()
            if repeat_calc == "y":
                iter += 1
            else:
                user_choice = input("Would you like to do another calculation: y or n").lower()
    
    elif calc_choice == "-":
        iter = 0
        while repeat_calc == "y":
            if iter > 0:
                minus_num1 = num_diffs
            else:
                minus_num1 = int(input("What is the first number: "))
            minus_num2 = int(input("What is the second number: "))
            num_diffs = minus_nums(minus_num1, minus_num2)
            print(f"result: {num_diffs}")
            repeat_calc = input("Would you like to reuse the result, and find another difference: y or n").lower()
            if repeat_calc == "y":
                iter += 1
            else:
                user_choice = input("Would you like to do another calculation: y or n").lower()

    elif calc_choice == "*":
        iter = 0
        while repeat_calc == "y":
            if iter > 0:
                mult_num1 = num_prods
            else:
                mult_num1 = int(input("What is the first number: "))
            mult_num2 = int(input("What is the second number: "))
            num_prods = mul_nums(mult_num1, mult_num2)
            print(f"result: {num_prods}")
            repeat_calc = input("Would you like to reuse the result, and find another product: y or n").lower()
            if repeat_calc == "y":
                iter += 1
            else:
                user_choice = input("Would you like to do another calculation: y or n").lower()

    elif calc_choice == "/":
        iter = 0
        while repeat_calc == "y":
            if iter > 0:
                div_num1 = num_quots
            else:
                div_num1 = int(input("What is the first number: "))
            div_num2 = int(input("What is the second number: "))
            num_quots = div_nums(div_num1, div_num2)
            print(f"result: {num_quots}")
            repeat_calc = input("Would you like to reuse the result, and find another quotient: y or n").lower()
            if repeat_calc == "y":
                iter += 1
            else:
                user_choice = input("Would you like to do another calculation: y or n").lower()


print("ok, we'll see you later!")
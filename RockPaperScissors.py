import random

random_integer = random.randint(1,100)
random_float = random.random()
random_fiver = random_float*5

print(f"random int: {random_integer}")
print(f"random float: {random_float}")
print(f"rnadom 1 to 5: {random_fiver}")

orig_list = [1, 2, 3, 4, 5]

orig_list.append(6)

print(f"appended list: {orig_list}")

orig_list.extend([7, 8, 9])

print(f"extended list: {orig_list}")
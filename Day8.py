# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("This is greeting 1!")
    print("This is greeting 2!")
    print("This is greeting 3!")

greet()

def greet_with_name(name):
    print(f"It's glad to hear from you {name}!")

greet_with_name("Jam")

# paint coverage exercise
"""
# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  area_square = height * width
  num_cans = math.ceil(area_square/ cover)
  print(f"You'll need {num_cans} cans of paint.")



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
"""

# prime checker problem
"""
# Write your code below this line 👇
def prime_checker(number):
  num_squared = number*number
  is_prime = True
  for i in range(1,num_squared):
    # print(f"i: {i}")
    if i%number == 0:
      # print(f"i%number: {i%number}")
      if i != number:
        # print(f"is i same? i: {i}")
        is_prime = False
      else:
        break
  if is_prime == True:
    print(f"It's a prime number.")
  else:
    print(f"It's not a prime number.")



# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
"""
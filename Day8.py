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
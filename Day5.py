fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)

# Average student heights

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

height_sum = 0

for student in student_heights:
  height_sum += student

avg = round(height_sum/ len(student_heights))

print(f"total height = {height_sum}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {avg}")

# Highest score problem
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_num = 0

for score in student_scores:
  if max_num < score:
    max_num = score

print(f"The highest score in the class is: {max_num}")

# Adding Even numbers

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

total = 0
for num in range(2,target+1,2):
  # print(f"num: {num}")
  total += num

print(total)

# FizzBuzz problem
for num in range(1,101):
  if num%3 == 0 and num%5== 0:
    print("FizzBuzz")
  elif num%5 == 0:
    print("Buzz")
  elif num%3 == 0:
    print("Fizz")
  else:
    print(num)
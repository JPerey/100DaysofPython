programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again.",
                          }

print(programming_dictionary["Loop"])

programming_dictionary["Syntax"] = "The way your program is written. Usually it is better to have more efficient syntax."

print(programming_dictionary)

# Dictionary practice problem
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  if student_scores[student] <= 100 and student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] <= 90 and student_scores[student] > 80:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] <= 80 and student_scores[student] > 70:
    student_grades[student] = "Acceptable"
  elif student_scores[student] <= 70:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
'''

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

Travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
}

# nesting dictionary practice

'''
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country,times_visited,cities_visited):
  new_log_entry = {
    "country": country,
    "visits": times_visited,
    "cities": cities_visited,
  }
  travel_log.append(new_log_entry)
  

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
'''
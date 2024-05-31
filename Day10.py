def format_name(f_name, l_name):
    full_name = f_name.title() + " " + l_name.title()

    return full_name

test_result = format_name("JAM", "PEREY")

print(test_result)

#leap year problem

'''
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_result = is_leap(year)
  # print(f"leap result = {leap_result}")
  if leap_result == True and (month-1) == 1:
    return 29
  else:
    return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

'''
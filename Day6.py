print("Hello")
num_char = len("Hello")
print(num_char)

# Creating a function

def my_function():
    print("Hello")
    print("Bye")

# running the function

my_function()

# Reeborgs example function
'''
def turn_right ( ):
    turn_left()
    turn_left()
    turn_left()

def move_two ( ):
    move()
    move()

def get_news():
    turn_left()
    move()
    turn_right()
    move_two()
    turn_left()
    move()
    turn_right()
    move_two()
    turn_left()
    move()
    turn_right()
    move_two()
    
    
get_news()
take()
'''

# Random hurdles problem

'''
def jump ( ):
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

while at_goal() == False:
    jump()
'''

# solving the random maze problem on reeborgs world

'''
def turn_right():
        turn_left()
        turn_left()
        turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''
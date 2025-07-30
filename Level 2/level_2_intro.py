#################################################
#                                               #
#               LEVEL 2 INTRO                   #
#                                               #
#################################################

'''
LEVEL 2 CHALLENGE - DO WE BAN THIS GUY?
    Write a function that reads a Twitch Chat message and decides whether to ban the guy.
    If the twitch message is "bald", then your function should return True
    If the twitch message is ANYTHING else, then your function should return False

NEW CONCEPTS 

    Variables
        Variable is a way to store a value.
        Think of it like a bucket that contains something inside, like a sentence or a number.
        To keep it simple for now, think of it like a bucket, and the code can pass that bucket around to different parts of the code.
        We'll use it in this level to represent the twitch chat message, and to represent the ban result 

    If statements
        Sometimes you only want code to happen in certain situations.
        For example, let's say you want to run some ban code that ONLY happens if someone says a bad message in chat!
        So an If statement will check is something is true, and if so, then the code inside will run
        We'll use it in this level to make the function act differently depending on the twitch chat message

    Functions
        So far your code just runs from top to bottom, one time.
        But what if you want to run a section of code multiple times, in slightly different ways?
        A "function" is mini-program that you can write one time, then use over and over.
        Think of it like a little helper that will do work for you.
        Usually a function looks like "function_name()".
        The () tells you what goes INTO the function.
'''

# This is a variable!
# The variable is named my_variable, and it has a value of "doug"
# Variable are useful for storing values and using them in various ways.
my_variable = "doug"

# This is an if statement! 
# In these examples, it uses == to check if two strings are the same.
if my_variable == "doug":
    print ('This code will run, because my_variable equals "doug"')
    
if my_variable == "john":
    print ('This code wont run, because my_variable doesnt equal "john"')

# This is a function!
# It is a little block of code that you can use it later whenever you want.
# In this case, the name of the function is "my_cool_function"
def my_cool_function(message):

    # Inside of the function, you can do whatever you want

    # For this particular function, it takes in a "message" variable
    # So now we can do stuff with the "message" variable, like print it
    print(message)

    # At the end of the function, you can optionally return something
    # This is providing something back to whoever called this function
    return "This is my return string"

# Now here's an example of calling the function!
test_message = "atrioc is bald"
result = my_cool_function(test_message)

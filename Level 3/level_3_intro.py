import random

#################################################
#                                               #
#               LEVEL 3 INTRO                   #
#                                               #
#################################################

'''
LEVEL 3 CHALLENGE - MAKING A CHAT BOT
    Write a function that reads a Twitch Chat message and calculates how long to ban the person.
    A time of 0 means they won't be banned. A time between 1 and 1,000,000 will ban them for that many seconds.
    Create the most interesting chat rule you can!

NEW CONCEPTS 

    Analyzing a string
        In the previous level, we checked if two strings are exactly the same.
        But you can analyze a string in all sorts of other ways!
        Examples are below - you can use these in combination with each other to create custom rules.

    If Else statements
        With an "if" statement, you guarantee that code only runs if a certain condition is met
        But you can add an "else" statement after it, which means the code will run if the condition is NOT met.
        Think of it as "if this is true, Code A will run, else, Code B will run"
'''


# Here are some examples of different ways of analyzing a message!

message = "this is an example twitch chat message"

# You can check if two strings are equal (This is what we did the previous level)
if message == "bald":
    ban_time = 100000

# You can check if two strings are NOT equal
if message != "bald":
    ban_time = 35

# This is an "if else" statement, where you can decide what happens if a condition is NOT met.
if message == "i love lemonade stand":
    ban_time = 0
else:
    ban_time = 100

# You can check the length of a string!

# Ban if the message is longer than 50 characters
if len(message) > 10:
    ban_time = 100  

# Or, can ban if the message is too short
if len(message) < 10:
    ban_time = 500  

# You can check if the string starts with specific letter or word!
if message.startswith("fuck"):
    ban_time = 1000
if message.startswith("I hate you because"):
    ban_time = 350

# You can check if a string contains a word or letter inside of it!
if "bald" in message:
    ban_time = 999
if "you are bald" in message:
    ban_time = 50

# You can go crazy and check the number of times a certain word or letter is inside the string
# For example, count how many times "bald" appears in the message:
bald_count = message.count("bald")
if bald_count > 3:
    ban_time = 1000  # Ban if "bald" appears more than three times

# You can also count single letters:
a_count = message.count("e")
if a_count > 0:
    ban_time = 500  # Ban if they used the letter 'e' a single time

# You can get the total number of words in a message
word_list = message.split() # This splits the message into words
word_count = len(word_list) # This counts the number of words
if word_count < 5:
    ban_time = 10000

# You can generate a random number, and use that to make something unpredictable
random_number = random.randint(1, 10)
if random_number == 10:
    ban_time = 1000 # This guy got unlucky


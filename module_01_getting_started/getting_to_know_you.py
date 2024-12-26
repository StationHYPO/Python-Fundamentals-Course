# This is our first Python program! 
# We'll create a friendly program that asks questions and responds to the user

# First, let's greet the user with a welcome message
print("Welcome to My First Python Program!")
print("I'm excited to get to know you!")

# Now we'll ask for the user's name and store it in a variable
# The input() function waits for the user to type something and press Enter
name = input("What's your name? ")

# We can use the name variable in our response
print("It's wonderful to meet you,", name, "!")

# Let's get some more information
age = input("How old are you? ")

# We can combine multiple pieces of information in our response
print("Wow!", name, "you're", age, "years old!")

# Let's ask one more question
favorite_color = input("What's your favorite color? ")

# Now let's create a nice summary using all the information we collected
print("\nHere's what I learned about you:")
print("Your name is", name)
print("You are", age, "years old")
print("Your favorite color is", favorite_color)
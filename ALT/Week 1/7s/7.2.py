number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = input()
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer: 4

# What does '!=' mean?
  # Answer: Not equal

# How many variables are there in the code?
  # Answer: 3

# How can you tell which lines of code are inside the loop?
  # Answer: 4, 5, and 6

# How many times will the loop repeat?
  # Answer: Infitnetly until you get the number correctly

# What has to happen to make the program run the last line of code?
  # Answer: You have to guess the correct number

correct = 54
print("I am thinking of a number between 1-100. What is that Number?")
guess = int(input())
while guess != 54:
  print("That is incorrect! Now you must try again.")
  guess =  int(input())
print("Correct! You finally got it!")
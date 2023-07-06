'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: You would get the response "Too Low!"

# What happens if you input the guess '6'?
  # Answer: You would get the response "Too High!"

# What happens if you input the guess '5'?
  # Answer: You would get the response "Correct!"

# What happens if you input the guess '-5'?
  # Answer: You would get the response "Too Low!"

# What happens if you input the guess '0'?
  # Answer: You would get the response "Too Low!"

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: They mean greater than and less than

# What happens if you change line 5 to if guess = number: ?
  # Answer: Then it would create a variable

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: There would be a condition and if it was met then you would get the response that comes after the if statement



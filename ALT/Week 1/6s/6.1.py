# Example code 1

number = 7
# variable assigned
print("I have thought of a number between 1 and 10")
# message would pop once program is ran
guess = int(input("Can you guess what it is?"))
# You would type a number between 1 - 10
if guess == number:
  print("Correct!")
# You would get the message if you type the correct number
elif guess < number:
  print("Too Low!")
# You would get the message if you type a number that is lower than the assigned number
else:
  print("Too High!")
# You would get the message if you type a number that is higher than the assigned number
# Example code 2

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
# Variables assigned
if number1 > number2:
  print("Number 1 is bigger than number 2")
# Message would show if your first number is greater than your second number
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
# Message would show if your second number is greater than your first number
else:
  print("Both numbers are the same")
# Message would show if your first and second number are the same value


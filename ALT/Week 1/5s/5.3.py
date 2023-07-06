# Starter Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))
# You would get the option to guess a number which is shown to be 5

if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
# You would get the corresponding messages if the number you type is higher or lower than the correct number

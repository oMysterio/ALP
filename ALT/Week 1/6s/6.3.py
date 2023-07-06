# Starter Code

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
number3 = int(input("Please enter your last number"))

if number1 > number3 > number2:
  print("Number 3 is smaller than number 1 but bigger than number 2")
elif number1 < number3 < number2:
  print("Number 3 is bigger than number 1 but smaller than number 2")
elif number1 == number3 > number2:
  print("Number 3 is equal to number 1 while being bigger than number 2")
elif number1 == number3 < number2:
  print("Number 3 is equal to number 1 while being smaller than number 2")
elif number1 < number3 == number2:
  print("Number 3 is equal to number 2 while being bigger than number 1")
elif number1 > number3 == number2:
  print("Number 3 is equal to number 2 while being smaller than number 1")
else:
  print("All numbers are the same")

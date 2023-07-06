'''
Task - Predict and Run
This task contains three code examples.

Look at each example , study it carefully. Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms selection, condition and branch in your prediction.
'''

# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 
# The message "You are old enough to drive" will only show up if you type in an age that is larger than 18
# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 
# The message with false will appear as the output because num1 is not equal to 10.
# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
# You would be given the choice to choose a number. The code will then determine whether the number is correct, too high, or too low. It would then give you the corresponding messages. Correct! if you're right, Too Low! if you're too low, or Too High! if your number is too high
# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
# Outside the loop. Will ask you the question
answer = input() 
# You will get a space to type your answer to the question asked. (Outside of loop)
while answer != "Paris":
# Loop starts and will not stop if you type the incorrect answer
  print("Incorrect! Try again.")
# the message you will receive in every loop
  answer = input("What is the capital of France?")
# the program will ask you the same question until you get it right.

print("Correct!")
# the message you will receieve when you get the correct answer (getting out of the loop)
# Example code 2

counter = 1
# variable assigned
while counter < 5:
# Loops begins
  print("This code is inside the loop")
# message will show due to counter being equal to 1
  counter += 1
# the value of counter will be added by 1
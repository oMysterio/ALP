N = int(input("What was the score you got on your test? It can only work if you use a number between 1-100."))
Y = N < 40
if Y:
  print("Your grade is a U...")
  print("You need to retake this test in order to pass 1st grade.")
else:
  print("Congrats! You passed the test!")
if 40 <= N <= 68:
  print("You got a C.")
if 69 <= N <= 79:
  print("You got a B.")
if 80 <= N:
  print("Congrats! You got an A!")
'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''
name = input("Hello! My name is Bob. What is your name?")
print("Greetings "+ name + "! I will ask you 3 questions about yourself")
answer1 = input("Are you male/female/other?")
print("Oh wow "+ name + "! I'm also a "+ answer1)
answer2 = input("How old are you?")
print("Haha I'm wayyyyy older than "+ answer2)
answer3 = input("What is your hobby?")
print("eh, I don't really like "+ answer3)
print("So you're "+ name + " who is a "+ answer2 + answer1 + " who likes to "+ answer3)
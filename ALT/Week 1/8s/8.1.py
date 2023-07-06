'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
# Variable assigned
print(Sentence)
# All words would be shown
print(Sentence[1])
# Only the second word will show up
Sentence.append("life")
# Life will be added into the variable
Sentence[4] = "sunny"
# Sunny would be added on the fourth slot
print(Sentence[4])
# sunny would show up in the output
print(Sentence[0] + " " + Sentence[3])
# The first and 4th word will show p in the output
print(Sentence)
# All original and new words will be displayed
# Almost everything was predicted correctly. The only difference being that life was put at the end of the sequence of words and sunny replaced bright in the sequence.
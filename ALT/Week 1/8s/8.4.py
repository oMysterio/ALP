'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''
weapons = ["Excalibur" , "Slingshot"]
zombieweakness = weapons[1]
print("Welcome to your battle! Today you will fight a zombie.")
print("Please choose which weapon you would like to choose. 0 is for Excalibur and 1 is for a slingshot. Choose Wisley! Or you can press 2 and choose your own weapon.")
choice = int(input())
if choice == 2:
    newweapon = (input("Please choose a name for your new weapon"))
    weapons.append(newweapon)
else:
  print(weapons)
while choice != 1:
  print("You have not chosen the correct weapon. Please choose again.")
  choice = int(input("Enter a weapon you want to use for battle"))

  
    
print("You have successfully defeated the zombie!")
  
# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables
height = int(input("Choose your height"))
width = int(input("Choose your width"))
# Calculate the area & store the result in the area variable
area = int(height * width)
print(area)
# Output the area variable (converted to string)

length = int(input("Choose your length"))
width = int(input("Choose your width"))

perimeter = (length * 2 + width * 2)

print(perimeter)

total = int(input("How much did your meal cost?"))

tip = int(total * 0.20)
print("Your meal costs" , total , "and you are tipping us" , tip)

cubeheight = int(input("First, Enter the height of your cube"))
cubewidth = int(input("Next, Enter the width of your cube"))
cubelength = int(input("Lastly, Enter the length of your cube"))
volume = (cubeheight * cubewidth * cubelength)
surfacearea = ((cubelength * cubewidth + cubewidth * cubeheight + cubeheight * cubelength) * 2)
print("Your cuboid's volume is" , volume , "and your total surface area is" , surfacearea)
'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''
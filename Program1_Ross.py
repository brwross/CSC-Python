##Brian Ross Program 1 CSC 201
##Project 1
pyr = int(input("How many levels should the pyramid have? "))
block = str(input("What should be the building block? "))
for i in reversed(range(0, pyr)): #counts from 0 to the range defined by the user input
    for j in range(pyr-i): #counts to the user input minus the stage of the previous for loop
        print(block, end = " ") #adds a new line for every i between 0 and pyr
    print() #creates the pyramid output scheme
    
#Report 1: The program will accept any number of characters as building blocks since the block variable is interpreted as a string of user input.

##Project 2/3
triangle = int(input("How many levels should the pyramid have? ")) #user chooses how many tiers the pyramid will have
building_block = str(input("What should be the building block? ")) #user chooses a string of characters as the "building block" of the pyramid
for p in range(0, triangle+1): #counts from 0 to the range defined by the user input
    for j in range(triangle- p): #counts to the user input minus the stage of the previous for loop
        print(" ", end = " ") #prints until the value of the level of the pyramid minus 1
    for j in range(1, p): #puts the two halfs of the pyramid together
        print(building_block, end = " ") #the output displays the user's choice of building block and breaks to a new line  
    for p in range(p,0,-1): #makes the right half of the pyramid
        print(building_block, end = " ") #prints the right half of the pyramid with the user's building block
    print("\n") #new line

#Report 2: Just like in project 1, the building block variable is interpreted as a string of characters. Thus providing significant more freedom for the user's input. 

##Project 3
for x in range(-15, 15, 1): #the interval for the loop is from -15 to 15 in incriments of 1
    y = round(x**2/4) #this is the function for the sideways parabola on the interval stated above
    print(' ' * y + '*') #prints the number of spaces coinciding with the value of the y function plus an asterisk

for k in reversed(range(0, 10, 1)): #counts from 9 to 0
    g = round(2*k**(1/2)) #the right-side transformaion of the previous y-function
    print('*'+ ' '*g + '*') #prints the right half of the parabola in the upright position
    print('\n\n\n') #whole bunch of new lines, the output is cluttered

    
##Project 5
rad = int(input("Choose the raius of the semi-cirlce"))#prompts the user for a value to be the circle's radius
for r in range(rad, 1, -1): #the range is the user's chosen value to 1, this creats the first quadrant of the circle
    side = round((rad**2-r**2)**(1/2)) #this function creates the proper spacing for the right side of the circle   
    print( ' '*side + '*') #output creates side-number of spaces followed by an asterisk
for r in range(1, rad, 1): #this loop creats what would be the fourth quadrant if the circle was on the unit plane
    side = round((rad**2-r**2)**(1/2)) #same function as above with a different range
    print(' '*side + '*') #prints the designated number of spaces followed by an asterisk
print("*")
print('\n')

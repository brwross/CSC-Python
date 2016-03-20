def simpleExpressionIsValid(somestring):
    import re
    sign = bool(re.search("[^\d^\s^+^/^*^\d\.\d^-]", somestring))
    othersign = bool(re.search("[+-/*]", somestring))
    digit = bool(re.search("\d", somestring))
    if sign == False and othersign == True and digit == True:
        return "Valid Expression"
    else:
        return "Invalid Expression"

    


def evaluateSimpleExpression(somestring):
    if simpleExpressionIsValid(somestring) == "Valid Expression":
        if (somestring.find("+")) != -1 : #if the user input has a plus sign this section of the code will initiate
            left = somestring.find("+") #locates the position of the plus sign
            num1 = int(somestring[:left]) #identifies the characters to the left of the plus sign as an integer and assigns them to the variable num1
            print("first number: ",somestring[:left]) # prints the left integer
            num2 = str(somestring[left+1:]) #assigns the variable num2 to be the string of characters to the right of the plus sign
            num2 = int(num2) #assigns the characters to the right of the plus sign as integers
            print("second number: ",str.strip(somestring[left+1:])) #prints the right side of the expression without any extra white space
            print("arguement: +")
            mem1 = (somestring, "=", num1 + num2)
            memory.append(mem1)
            print(somestring, "=", num1 + num2) #prints the total expression and the calculation
            
        elif (somestring.find("-")) != -1 :#if the user input has a minus sign this section of the code will initiate
            left = somestring.find("-") #locates the position of the minus sign
              
            num1 = int(somestring[:left])#identifies the characters to the left of the minus sign as an integer and assigns them to the variable num1
            print("first number: ",somestring[:left])# prints the left integer
            num2 = str(somestring[left+1:])#assigns the variable num2 to be the string of characters to the right of the minus sign
            num2 = int(num2) #assigns the characters to the right of the minus sign as integers
            print("second number: ",str.strip(somestring[left+1:]))#prints the right side of the expression without any extra white space
            print("arguement: -")
            mem2 = (somestring, "=", num1 - num2)
            memory.append(mem2)
            
            print(somestring, "=", num1 - num2)#prints the total expression and the calculation
            
        elif (somestring.find("*"))!= -1 :#if the user input has a multiplication sign this section of the code will initiate
            left = somestring.find("*")#locates the position of the multiplication sign
            
            num1 = int(somestring[:left])#identifies the characters to the left of the multiplication sign as an integer and assigns them to the variable num1
            print("first number: ",somestring[:left])# prints the left integer
            num2 = str(somestring[left+1:])#assigns the variable num2 to be the string of characters to the right of the multiplication sign
            num2 = int(num2)#assigns the characters to the right of the multiplication sign as integers
            print("second number: ",str.strip(somestring[left+1:]))#prints the right side of the expression without any extra white space
            print("arguement: *")
            mem3 = (somestring, "=", num1 * num2)
            memory.append(mem3)
            print(somestring, "=", num1 * num2)#prints the total expression and the calculation
        
        elif (somestring.find("/"))!= -1 :#if the user input has a division sign this section of the code will initiate
            left = somestring.find("/")#locates the position of the division sign
            
            num1 = int(somestring[:left])#identifies the characters to the left of the division sign as an integer and assigns them to the variable num1
            print("first number: ",somestring[:left])# prints the left integer
            num2 = str(somestring[left+1:])#assigns the variable num2 to be the string of characters to the right of the division sign
            num2 = int(num2)#assigns the characters to the right of the division sign as integers
            print("second number: ",str.strip(somestring[left+1:]))#prints the right side of the expression without any extra white space
            print("arguement: /")
            mem4 = (somestring, "=", num1 / num2)
            memory.append(mem4)
            print(somestring, "=", num1 / num2)#prints the total expression and the calculation
            
        else:
            print("Does not compute") #if the user doesn't input a usable expression the program will return "Does not compute"

    else:
        return "Invalid Expression, cannot evaluate"
    
memory = []
while(input("To end the program, type 'end'. Otherwise, hit enter") != "end"):
    
    
    
    somestring = input("Enter a simple expression in the form: number +/-* number ")

    print(evaluateSimpleExpression(somestring))

    inputs = input("would you like to see previous inputs? (Press Y/N) ")
    inputs = inputs.upper()
    
    if inputs == "Y" :
        list_number = int(input("How many? Please enter a number "))
        print(memory[-list_number:])
    else:
        print("\n")

#Brian Ross Lab 2 CSC 201
memory = []
while(True): #loop to automatically repeat the program
    k = input("Please enter an expression of the form ( number +/-* number ): ")#asks the user for the expression to be calculated
    para_arg1 = int(k.find("(")) #finds the index of the "(" sign
    para_arg2 = int(k.find(")")) #finds the index of the ")" sign
   
    if  para_arg1 > 0 :  ##this if/elif sequence is to determine if the user is using the proper input method. In this case an error will be printed if a "(" does not appear at the beginning of the input string
        print("invalid input")
    elif para_arg2 < para_arg1: #prints an error if the ")" sign comes before the "(" sign
        print("invalid input")
    elif para_arg2 != (len(k)-1): #prints an error if the ")" does not come at the end of the string
        print("invalid input")
    else:
        if (k.find("+")) != -1 : #if the user input has a plus sign this section of the code will initiate
            left = k.find("+") #locates the position of the plus sign
            sign = para_arg1 + 1
            num1 = int(k[sign:left]) #identifies the characters to the left of the plus sign as an integer and assigns them to the variable num1
            print(k[sign:left]) # prints the left integer
            num2 = str(k[left+1:para_arg2]) #assigns the variable num2 to be the string of characters to the right of the plus sign
            num2 = int(num2) #assigns the characters to the right of the plus sign as integers
            print(str.strip(k[left+1:para_arg2])) #prints the right side of the expression without any extra white space
            mem1 = (k, "=", num1 + num2)
            memory.append(mem1)
            print(k, "=", num1 + num2) #prints the total expression and the calculation
        
        elif (k.find("-")) != -1 :#if the user input has a minus sign this section of the code will initiate
            left = k.find("-") #locates the position of the minus sign
            sign = para_arg1 + 1 #finds the  
            num1 = int(k[sign:left])#identifies the characters to the left of the minus sign as an integer and assigns them to the variable num1
            print(k[sign:left])# prints the left integer
            num2 = str(k[left+1:para_arg2])#assigns the variable num2 to be the string of characters to the right of the minus sign
            num2 = int(num2) #assigns the characters to the right of the minus sign as integers
            print(str.strip(k[left+1:para_arg2]))#prints the right side of the expression without any extra white space
            mem2 = (k, "=", num1 - num2)
            memory.append(mem2)
            
            print(k, "=", num1 - num2)#prints the total expression and the calculation

        elif (k.find("*"))!= -1 :#if the user input has a multiplication sign this section of the code will initiate
            left = k.find("*")#locates the position of the multiplication sign
            sign = para_arg1 + 1
            
            num1 = int(k[sign:left])#identifies the characters to the left of the multiplication sign as an integer and assigns them to the variable num1
            print(k[sign:left])# prints the left integer
            num2 = str(k[left+1:para_arg2])#assigns the variable num2 to be the string of characters to the right of the multiplication sign
            num2 = int(num2)#assigns the characters to the right of the multiplication sign as integers
            print(str.strip(k[left+1:para_arg2]))#prints the right side of the expression without any extra white space
            mem3 = (k, "=", num1 * num2)
            memory.append(mem3)
            print(k, "=", num1 * num2)#prints the total expression and the calculation
        
        elif (k.find("/"))!= -1 :#if the user input has a division sign this section of the code will initiate
            left = k.find("/")#locates the position of the division sign
            sign = para_arg1 + 1
            num1 = int(k[sign:left])#identifies the characters to the left of the division sign as an integer and assigns them to the variable num1
            print(k[sign:left])# prints the left integer
            num2 = str(k[left+1:para_arg2])#assigns the variable num2 to be the string of characters to the right of the division sign
            num2 = int(num2)#assigns the characters to the right of the division sign as integers
            print(str.strip(k[left+1:para_arg2]))#prints the right side of the expression without any extra white space
            mem4 = (k, "=", num1 / num2)
            memory.append(mem4)
            print(k, "=", num1 / num2)#prints the total expression and the calculation
            
        else:
            print("Does not compute") #if the user doesn't input a usable expression the program will return "Does not compute"
        
    inputs = input("would you like to see previous inputs? (Press Y/N) ")
    inputs = inputs.upper()
    
    if inputs == "Y" :
        list_number = int(input("How many? Please enter a number "))
        print(memory[-list_number:])
    else:
        print("\n")

    user_input = input("End? Y/N?")
    user_input = user_input.upper()
    if user_input == "Y" :
        break


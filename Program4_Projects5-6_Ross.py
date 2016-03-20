def simpleExpressionIsValid(somestring):
    import re
    sign = bool(re.search("[^(^)^\d^\s^+^/^*^\d\.\d^-]", somestring)) ##checks for anything besides the [^(^)^\d^\s^+^/^*^\d\.\d^-] characters
    othersign = bool(re.search("[+-/*]", somestring))  ##somestring must contain an arguement
    digit = bool(re.search("\d", somestring)) ##somestring must contain a digit
    ##multi_args = bool(re.search("\)\*\(", somestring)) saving in case 
    more_conditions = bool(re.search("\*\ \(",somestring)) ##checks for incorrect formatting the crashes the program
    more_conditions2 = bool(re.search("\)\ \*",somestring))
    if more_conditions == True or more_conditions2 == True: ##if-else checks against the bools defined above to check for a valid or invalid statement
        return "Invalid expression"                             
    elif sign == False and othersign == True and digit == True :
        return "Valid Expression"
    else:
        return "Invalid Expression"



def evaluateSimpleExpression(somestring):
    
    if simpleExpressionIsValid(somestring) == "Valid Expression": #if simpleExpressionIsValid is valid compute the expressions
        
        import re
        
        args = re.split("\)\*\(", somestring) ##splits the string at all )*( 
        
        list_of_args = []
        for x in args: ##sends each expression in the string to list_of_args
            m = re.sub("[\(\)]"," ", x)
            list_of_args.append(m)
            
        memory = []
        for i in list_of_args:
            if (i.find("+")) != -1 : #if the user input has a plus sign this section of the code will initiate
                left = i.find("+") #locates the position of the plus sign
                num1 = int(i[:left]) #identifies the characters to the left of the plus sign as an integer and assigns them to the variable num1
                ##print("first number: ",i[:left]) # prints the left integer
                num2 = str(i[left+1:]) #assigns the variable num2 to be the string of characters to the right of the plus sign
                num2 = int(num2) #assigns the characters to the right of the plus sign as integers
                ##print("second number: ",str.strip(i[left+1:])) #prints the right side of the expression without any extra white space
                ##print("arguement: +")
                mem1 = (num1 + num2)
                memory.append(mem1)
                ##print(i, "=", num1 + num2) #prints the total expression and the calculation
                
            elif (i.find("-")) != -1 :#if the user input has a minus sign this section of the code will initiate
                left = i.find("-") #locates the position of the minus sign
                  
                num1 = int(i[:left])#identifies the characters to the left of the minus sign as an integer and assigns them to the variable num1
                ##print("first number: ",i[:left])# prints the left integer
                num2 = str(i[left+1:])#assigns the variable num2 to be the string of characters to the right of the minus sign
                num2 = int(num2) #assigns the characters to the right of the minus sign as integers
                ##print("second number: ",str.strip(i[left+1:]))#prints the right side of the expression without any extra white space
                ##print("arguement: -")
                mem2 = (num1 - num2)
                memory.append(mem2)
                
                ##print(i, "=", num1 - num2)#prints the total expression and the calculation
                
            elif (i.find("*"))!= -1 :#if the user input has a multiplication sign this section of the code will initiate

                left = i.find("*")#locates the position of the multiplication sign
                
                num1 = int(i[:left])#identifies the characters to the left of the multiplication sign as an integer and assigns them to the variable num1
                ##print("first number: ",i[:left])# prints the left integer
                num2 = str(i[left+1:])#assigns the variable num2 to be the string of characters to the right of the multiplication sign
                num2 = int(num2)#assigns the characters to the right of the multiplication sign as integers
               ## print("second number: ",str.strip(i[left+1:]))#prints the right side of the expression without any extra white space
                ##print("arguement: *")
                mem3 = (num1 * num2)
                memory.append(mem3)
                ##print(i, "=", num1 * num2)#prints the total expression and the calculation
            
            elif (i.find("/"))!= -1 :#if the user input has a division sign this section of the code will initiate
                left = i.find("/")#locates the position of the division sign
                
                num1 = int(i[:left])#identifies the characters to the left of the division sign as an integer and assigns them to the variable num1
                ##print("first number: ",i[:left])# prints the left integer
                num2 = str(i[left+1:])#assigns the variable num2 to be the string of characters to the right of the division sign
                num2 = int(num2)#assigns the characters to the right of the division sign as integers
                ##print("second number: ",str.strip(i[left+1:]))#prints the right side of the expression without any extra white space
                ##print("arguement: /")
                mem4 = (num1 / num2)
                memory.append(mem4)
                ##print(i, "=", num1 / num2)#prints the total expression and the calculation
                
            else:
                print("Invalid Expression. Does not compute") #if the user doesn't input a usable expression the program will return "Does not compute"
        
        some_constant = 1
        for n in memory : ##used to multiply contents of the string together
            some_constant = n*some_constant
        print(somestring, "=")
        total_arguement = (somestring, some_constant) ##stores the original input and evalauation
        last_memory.append(total_arguement)
        
        return some_constant
    else:
        return "Try another expression"

end = input("Type 'end' to end the program. 'Enter' to continue. " )
last_memory = []
while end != "end" :
    
    string = input("Input an expression in the form of: (expression)*(expression)... where the expressions are made from number and a +-/* sign. For example, (5+4)*(3+7)*(200*55). Be sure to avoid spaces between expressions. Go ahead: ") 
    print(simpleExpressionIsValid(string))
    print(evaluateSimpleExpression(string))
    last = input("Type 'last' to see all previous inputs ")
    if last == "last":
        print(last_memory)

#Brian Ross Program 3 Part 2
#indexs through the two dna sequences to determine the number of individual matches in each string
def NumMatches(gen,gen2):
    import re #import regex
    a = "a" #assigns variable values to strings
    g = "g"
    t = "t"
    c = "c"

    as1 = list() #index values of the instances of the variable
    as2 = list()
    gs2 = list()
    gs1 = list()
    ts1 = list()
    ts2 = list()
    cs1 = list()
    cs2 = list()
    find = -1 #starting point for the iteration
    while True: #iterates through the string to find the index values of "a" that will be appeded to list as2 
        find = gen2.find("a", find+1)
        as2.append(find)
        if find == -1: #if no more instances can be found the loop ends
            break
    while True: #same as above 
        find = gen2.find("g", find+1)
        gs2.append(find)
        if find == -1:
            break
    while True:
        find = gen2.find("t", find+1)
        ts2.append(find)
        if find == -1:
            break
    while True:
        find = gen2.find("c", find+1)
        cs2.append(find)
        if find == -1:
            break
    while True:
        find = gen.find("a", find+1)
        as1.append(find)
        if find == -1:
            break
    while True:
        find = gen.find("g", find+1)
        gs1.append(find)
        if find == -1:
            break
    while True:
        find = gen.find("t", find+1)
        ts1.append(find)
        if find == -1:
            break
    while True:
        find = gen.find("c", find+1)
        cs1.append(find)
        if find == -1:
            break
    as1.remove(-1)#removes the instance of "-1" from each 
    gs1.remove(-1)
    cs1.remove(-1)
    ts1.remove(-1)
    as2.remove(-1)
    gs2.remove(-1)
    ts2.remove(-1)
    cs2.remove(-1)
    as3 = set(as1).intersection(as2) #creates a set of values in both as1 and as2
    gs3 = set(gs1).intersection(gs2)
    ts3 = set(ts1).intersection(ts2)
    cs3 = set(cs1).intersection(cs2)
    numMatches = len(cs3)+len(ts3)+len(gs3)+len(as3) #the length of the set is the number of matches between the two strings
    return "There are %d matches between the two sequences" %numMatches


gen = input("Choose a DNA string") #placeholder for gene sequence
gen2 = input("Choose a second DNA string")
print(NumMatches(gen,gen2))

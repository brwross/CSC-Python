#Brian Ross Program 3 projects 1-4
#takes a genes sequence with characters g,c,t,a and transposes it to the corresponding base pair
def transpose(genes):
    genes = genes.replace("g","m") #uses placeholder letters in order to match base pairs
    genes = genes.replace("c","n")
    genes = genes.replace("a","o")
    genes = genes.replace("t","p")
    genes = genes.replace("m","c")
    genes = genes.replace("n","g")
    genes = genes.replace("o","t")
    genes = genes.replace("p","a")
    return(genes)

#creates a mirror image of the string
def flip(genes):
    return(genes[::-1]) #swaps the index from front to back

#determines if there are characters besides g,c,t,a in the string
def valid(genes):
    length = len(genes) #takes the length of te string
    num_a = genes.count("a") #counts the instances of "a"
    num_c = genes.count("c")
    num_t = genes.count("t")
    num_g = genes.count("g")
    if (length - num_a - num_c - num_t - num_g == 0): #the length of the string should be the summation of the instances of g,c,t,and a. 
        return "Valid"
    else:
        return "Invalid"

#compares two strings using the preceeding functions and appends the values of those functions to a readable list    
def two_valid(genes1, genes2):
    sequence1 = list() #list that will contain the results of one of the sequences
    sequence2 = list()
    a = valid(genes1) #assigns a variable to the validity of the functions
    sequence1.append(a)
    b = valid(genes2)
    sequence2.append(b)
    c = flip(genes1)
    sequence1.append(c)
    d = flip(genes2)
    sequence2.append(d)
    e = transpose(genes1)
    sequence1.append(e)
    f = transpose(genes2)
    sequence2.append(f)
    print("Gene sequence 1 :",sequence1,"\n","Gene sequence 2 :",sequence2)
    if str(e) == str(f): #if the transposed strings are the same then the dna fragments must also be the same
        return "DNA match"
    else:
        return "Does not match"
    
##gen = "gcta"
#gen = "gtaaaaacgtcagtgctagagatctcta"
#gen2 = "gtcacagth"
gen = "gtca" #sample gene sequences
gen2 = "gtca"
print("gene sequence","\n",gen,"\n")
print("transposed gene sequence")
print(transpose(gen),"\n")
print("flipped gene sequence")
print(flip(gen),"\n")
print("verification of gene sequence")
print(valid(gen),"\n")
print("comparing two gene sequences","\n")
print(two_valid(gen,gen2))

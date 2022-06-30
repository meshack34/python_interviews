# test = int(input("Enter numbers : "))
test = 8
for j in range (test):  # for rows
    for k in range (j,test): # for columns 
        print("", end =" ")
    for l in range (j+1): # for columns 
        print("/_", end =" ")
    for m in range (j-2): # for columns 
        print("", end =" ")
    print( )
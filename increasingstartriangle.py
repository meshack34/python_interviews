# test = int(input("Enter numbers : "))
test = 4
for j in range (test):  # for rows
    for k in range (j,test): # for columns 
        print("m", end =" ")
    for l in range (j+1): # for columns 
        print("x", end =" ")
    for m in range (j): # for columns 
        print("x", end =" ")
    print( )
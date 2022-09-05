n=int (input("Enter num: "));
m=int( input("Enter num: "));

def tri_recursion(k,y):
    sum=(k+y)
    print("The sum is : " + str(sum))
    
    multiply=(k*y)
    print("The multiply is : " + str(multiply))
    
    Division=(k/y)
    print("The Division is : " + str(Division))
    
    substraction=(k-y)
    print("The substraction is : " + str(substraction))
    
(tri_recursion(m,n)) #call

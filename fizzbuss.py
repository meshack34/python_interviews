m=int(input("Enter num: "))
for i in range(m):
    if (i%2==0 and i%3==0):
        print(' FizzBuzz')
        continue
    elif(i%2 ==0 ):
        print( " fizz")
        continue
    
    elif(i%3==0):
        print("Buzz")
        continue
    else:
        print(i)
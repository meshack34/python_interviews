
s= int(input("Enter Number: "))

for i in range(s+1):
    print("*"* (i+1))
    for k in range(i**i):
     print("*"* (i))
    
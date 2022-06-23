# prompt user to enter number , 
# loop through number on single line 
# starting at 1 to largest and 
# from largest back to one 

# i.e 12345678987654321

number = int (input("Enter number : "))

for i in range (1,number+1):
    print(str(i), end="")
for i in range (number-1, 1 ,-1):
    print(str(i), )
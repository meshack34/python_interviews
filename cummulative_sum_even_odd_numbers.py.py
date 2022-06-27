# Question 1
# Apython function which prompt user to enter a number as range and to 
# print even and odd number then total for even and odd numbers

sum = 0
sumodd =0
counter= int (input("enter num: "))
for i in range(counter):
    if (i % 2==0):
        sum = sum +i
        print(str(i)+ '', "even")
    else:
        sumodd = sumodd +i
        print(str(i)+ '', "odd")
print ("Total odd:" +str(sumodd))
print ("Total even:" + str(sum))

# Apython function which prompt user to enter a number as range and to 
# print cummulative even and odd number then total for even and odd numbers


sum = 0
sumodd =0
counter= int (input("enter num"))
for i in range(counter):
    if (i % 2==0):
        sum = sum +i
        print(str(sum)+ '', "even")
    else:
        sumodd = sumodd +i
        print(str(sumodd)+ '', "odd")
print ("Total odd:" +str(sumodd))
print ("Total even:" + str(sum))
# output 110
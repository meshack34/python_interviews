x = int (input("Enter number : "))
y = int (input("Enter number : "))
muli=(x*y)
sum = (x+y)
divide=(x/y)
print ("The division of " +str(x) ,"by " +str(y) + " = " + str(divide))
print ("The sum of " +str(x) ,"and " +str(y) + " = " + str(sum))
print ("The muli of " +str(x) ,"and " +str(y) + " = " + str(muli))



weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']

listAsString = ' '.join(weekdays) #convert to string
listAsTuple = tuple(weekdays)  #convert to tuple
listAsSet = set(weekdays)  #convert to set
print(listAsSet)
print(listAsString)
print(listAsTuple)
print(weekdays.count('mon')) #count occurence a particular element in the list?
for x in set(weekdays):
    print(x,weekdays.count(x))

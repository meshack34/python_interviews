# Python program to display all the prime numbers within an interval

lower = 0
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
  if num >1 :
       for i in range(2, num):
           if (num % i == 0 and i> 1):
               break
       else:
              print(num, end='     ')
             
# set avariable called lower to 5 and higher to 12. 
# prompt user to enter a number. if number less than 5 print less fit, 
# if higher than 12 print high fit. if beetween 5 and 12 should print fits.
# this loop should continue till the number that fit 5 and 12 found
lower=5
higher=12
loop= True

while(loop):
    m= int(input("Enter a avariable : "))
    if (lower <=m <=higher):
        loop=False
        print("Fits well")
    else:
        print("outside fits")
print("Fits well")
        

        
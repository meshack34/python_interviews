# let user enter a number loop through 
# the number and print flip and flop

word ="flip"
counter = int(input("enter a number: "))
for i in range (counter):
    if (word == "flip"):
        word= ("flop")
    else:
        word=("flip")
        
    print(str(i) + word)
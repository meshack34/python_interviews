# user enter number and stars printed as follows
# *
# **
# ***
# ****
# *****
# ******
# ****
# ***
# **
# *

s= int(input("Enter Number: "))

for i in range(s+1):
    print("*"* (i+1))

for i in range(s-1,0, -1):
    print("*"* (i))
    
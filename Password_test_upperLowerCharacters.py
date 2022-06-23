# prompt user to enter new password
# password must be 8 characters 
# must have both lower and capital letters




password_length = 8
loop= True
while(loop):
    p = input("Enter new password: ")
    password_upper= p.upper()
    password_lower= p.lower()
    p_count= len(p)
    if ( (p==p.lower())or (p.upper()==p) or (password_length)<len(p) ):
        print("wrong password")
    else:
        loop= False
        print("cool")
  
    
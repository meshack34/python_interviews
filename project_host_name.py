# alpha,beta, gamma
# dev,test,pro

for i in ("alpha","beta", "gamma"):
    for k in ("dev","test","pro"):
        if k == "pro":
            prowlsize = 4
        else :
            prowlsize = 1
        for m in range(prowlsize):
            print(str(i)+"-"+ str(k) +"-0" +" ", str(m+1), end="")
            
    print()
           
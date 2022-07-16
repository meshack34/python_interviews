nums=8
for i in range(nums):
    for k in range(nums):
        print("" , end=' ')
    for l in range(i):
        print("*" , end=' ')
        for c in range(nums+1):
          print("l" , end=' ')
    print()
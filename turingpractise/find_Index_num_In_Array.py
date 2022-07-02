
c=int(input('Enter num: '))
b=[65,1,3,5,7,8,80,2]
def add_arrays(nums,num2):
    for i,targetn in enumerate(nums):
        if targetn == num2 :
          print(i)
    return i
    # Return after all execution
    print("-1")
    
add_arrays(b,c)
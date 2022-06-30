data1 = [1, 2, 3]
data2 = [4, 5, 6]
ourdog = {"cool":"mes", "donkk5":5, "temb6":"mmmm"}

data = data1 + data2
print (ourdog["cool"])

print(data)
a=[1,2,3,4,5,6]
b=[7,8,9,10,11,12]

def add_arrays(a,b):
    c=[]
    for array1, array2 in zip(a,b):
      c.append(array1+array2)
    print(c)
    return c # Return after all execution
     


#add_arrays(a,b)
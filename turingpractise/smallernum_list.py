# lista=[1,2,3,4,5,6]
# class Solution:
#     def __init__(self, nums:List[int]):
#         output = []
#     for i in range (len(nums)):
#         count = 0
#         for j in range (len(nums)):
#             if j != i and nums[j]<nums[i] :
#                 count += 1
            # output.append(count)


b=[10,5,5,8,7]
class Solution:
    def add_arrays(nums):
        c=[]
        for i in range(len(nums)):
            count = 0
            for j in range (len(nums)):
                if nums[j]>nums[i] :
                    count += 1
            c.append(count)
        print(c)
        return c # Return after all execution
     
        
    
    add_arrays(b)
#add_arrays(a,b)
            
                 
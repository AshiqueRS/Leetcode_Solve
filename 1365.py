nums = [8,1,2,2,3]
actual_nums=nums.copy()
nums.sort()
output= {}
ele=[]
l=[]
numbers=len(ele)
ele.append(nums[0])
output[nums[0]]=numbers
for i in range(1,len(nums)):
    if nums[i]==nums[i-1]:
        output[nums[i]]=numbers
    else:
        output[nums[i]]=len(ele)
        numbers=len(ele)
        
    ele.append(nums[i]) 
for i in actual_nums:
    l.append(output[i])

print(l)
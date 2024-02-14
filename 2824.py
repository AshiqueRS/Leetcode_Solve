nums = [-1,1,2,3,1]
target = 2
count = 0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if 0<=i<j<len(nums) and nums[i]+nums[j]<target:
            count+=1
print(count)
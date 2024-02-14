import math
nums = [[1,2,3],[5,6,7],[9,10,11]]
l =[]
m=0
def prime(x):
    flag =0
    if x ==1:
        flag = 1
    for i in range(2,(math.floor(math.sqrt(x))+1)):
        if x%i==0:
            flag = 1
    if flag==1:
        return False
    else:
        return True

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if i == j or i+j==len(nums)-1:
            if nums[i][j]>m:
                if prime(nums[i][j]) == True:
                    m = nums[i][j]

print(m)
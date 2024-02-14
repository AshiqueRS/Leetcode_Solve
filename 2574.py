nums = [10,4,8,3]
l =[]
count =0
for i in range(len(nums)):
    count +=nums[i]
    l.append(count)
for i in range(len(nums)):
    if i==0:
        nums[i]= abs((l[len(l)-1]-l[i]))
    elif i== (len(nums)-1):
        nums[i] = abs(l[len(l)-2])
    else:
        nums[i] = abs(l[i-1]-(l[len(l)-1] -l[i]))
print(nums)
nums = [3,1,-2,-5,2,-4]
p = []
n = []
for i in nums:
    if i > 0:
        p.append(i)
        p.append('')
    else:
        n.append('')
        n.append(i)
for i in range(len(nums)):
    if i%2 == 0:
        nums[i] = p[i]
    else:
        nums[i] = n[i]
print(nums)
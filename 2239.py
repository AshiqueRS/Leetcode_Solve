nums = [-4,-2,1,4,8]
x = 100000
for i in nums:
    if x > abs(i):
        x= abs(i)
if x in nums:
    print(x)
else:
    print(-x)
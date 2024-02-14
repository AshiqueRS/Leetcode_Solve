nums = [1,2,3,1]
hashset = set()
for n in nums:
    if n in hashset:
        print(True) 
    hashset.add(n)
print(False) 
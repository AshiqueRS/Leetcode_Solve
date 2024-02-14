accounts = [[1,2,3],[3,2,1]]
l = []
for i in range(len(accounts)):
    sum = 0
    for j in range(len(accounts[i])):
        sum += accounts[i][j]  
    l.append(sum)
print(max(l))
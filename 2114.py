sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
lst = []
for i in sentences:
    lst.append(len(i.split(' '))) 
print(max(lst))
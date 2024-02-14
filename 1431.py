candies = [2,3,5,1,3]
extraCandies = 3
a = max(candies)
for i in range(len(candies)):
    if a <= candies[i]+extraCandies:
        candies[i]= True
    else:
        candies[i] = False
print(candies)
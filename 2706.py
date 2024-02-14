prices = [1,2,2]
money = 3
prices.sort()
if money >= prices[0]+prices[1]:
    print((money - (prices[0]+prices[1])))
else:
    print(money) 
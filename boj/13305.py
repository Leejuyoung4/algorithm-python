n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
result = min_price * road[0]

for i in range(1, n - 1):
    min_price = min(min_price, price[i])
    result += min_price * road[i]
    
print(result)
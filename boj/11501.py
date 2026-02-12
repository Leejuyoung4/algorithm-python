T = int(input())

for _ in range(T):
    n = int(input())
    num = list(map(int, input().split()))

    max_price = 0
    total = 0

    for i in range(n - 1, -1, -1):
        if num[i] > max_price:
            max_price = num[i]
        else:
            total += max_price - num[i]

    print(total)
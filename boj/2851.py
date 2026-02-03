total = 0
temp = 0

for _ in range(10):
    score = int(input())
    total += score

    if total > 100:
        temp = total - score
        break

if abs(temp - 100) > abs(total - 100):
    print(total)
elif abs(temp - 100) < abs(total - 100):
    print(temp)
elif abs(temp - 100) == abs(total - 100):
    print(max(temp, total))
n = int(input())
m = int(input())
light = list(map(int, input().split()))

answer = max(light[0], n - light[-1])

for i in range(1, m):
    gap = light[i] - light[i - 1]
    answer = max(answer, (gap + 1) // 2)

print(answer)
L = int(input())
N = int(input())

cake = [0] * (L + 1)
cnt = [0] * (N + 1)
expected = 0
result1 = 0

for idx in range(1, N + 1):
    P, K = map(int, input().split())

    if K - P + 1 > expected:
        expected = K - P + 1
        result1 = idx

    for i in range(P, K + 1):
        if cake[i] == 0:
            cake[i] = idx

for i in range(1, len(cake)):
    temp = cake[i]
    if temp != 0:
        cnt[temp] += 1

for i in range(1, len(cnt)):
    if cnt[i] == max(cnt):
        result2 = i
        break

print(result1)
print(result2)
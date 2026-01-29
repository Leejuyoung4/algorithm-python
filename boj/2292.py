N = int(input())

sum = 1
cnt = 1

while sum < N:
    sum = sum + 6 * cnt
    cnt += 1

print(cnt)
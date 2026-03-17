import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name = []
limit = []

for _ in range(n):
    s, sup = input().split()
    sup = int(sup)
    name.append(s)
    limit.append(sup)

for _ in range(m):
    power = int(input())

    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if power <= limit[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print(name[start])
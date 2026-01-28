n = int(input())
switch = [0] + list(map(int, input().split()))

m = int(input())
for _ in range(m):
    gender, num = map(int, input().split())

    if gender == 1:
        i = num
        while i <= n:
            switch[i] = 1 - switch[i]
            i +=  num

    elif gender == 2:
        left = right = num
        while left - 1 >= 1 and right + 1 <= n and switch[left - 1] == switch[right + 1]:
            left -= 1
            right += 1
        for i in range(left, right + 1):
            switch[i] = 1 - switch[i]

for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
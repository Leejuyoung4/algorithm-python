N = int(input())
seat = list(input())

cnt = 1
temp = 0

for i in range(N):
    if seat[i] == 'S':
        cnt += 1
    elif seat[i] == 'L':
        temp += 1
        if temp % 2 != 0:
            cnt += 1

print(min(N, cnt))
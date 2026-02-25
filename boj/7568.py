n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

idx = 0
rank = []
while idx != n:
    cnt = 1
    for i in range(n):
        if arr[idx][0] < arr[i][0] and arr[idx][1] < arr[i][1]:
            cnt += 1
    rank.append(cnt)
    idx += 1

for r in rank:
    print(r, end=" ")
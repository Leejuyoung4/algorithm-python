p = int(input())

for _ in range(p):
    data = list(map(int, input().split()))
    t = data[0]
    height = data[1:]

    line = []
    cnt = 0

    for h in height:
        idx = 0
        while idx < len(line) and line[idx] < h:
            idx += 1
        
        cnt += len(line) - idx
        line.insert(idx, h)

    print(t, cnt)
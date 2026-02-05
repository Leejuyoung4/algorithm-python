N = int(input())
grid = [[0] * 1001 for _ in range(1001)]

# 색종이 칠하기
idx = 0

for _ in range(N):
    x, y, x_len, y_len = map(int, input().split())
    idx += 1
    for r in range(x, x + x_len):
        for c in range(y, y + y_len):
            grid[r][c] = idx

# 색종이 넓이 구하기
area = [0] * (N + 1)

for idx in range(1, N + 1):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == idx:
                area[idx] += 1

for i in range(1, len(area)):
    print(area[i])
word = list(input())
N = len(word)

for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        r = i
        c = N // i

idx = 0

grid = [[None] * c for _ in range(r)]
for j in range(c):
    for i in range(r):
            grid[i][j] = word[idx]
            idx += 1

for i in range(r):
     for j in range(c):
          print(grid[i][j], end="")
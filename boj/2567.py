n = int(input())
board = [[0] * 100 for _ in range(100)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    # 색종이 칠하기
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if board[i][j] == 0:
                board[i][j] = 1
    
# 색종이 둘레 구하기
for i in range(100):
    for j in range(100):
        # 색종이가 칠해진 부분 사방탐색
        if board[i][j] == 1:
            for k in range(4):
                nr = i + dx[k]
                nc = j + dy[k]

                if nr < 0 or nr >= 100 or nc < 0 or nc >= 100 or board[nr][nc] == 0:
                    cnt += 1

print(cnt)
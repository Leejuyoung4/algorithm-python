n = int(input())
grid = [list(input()) for _ in range(n)]

left_arm, right_arm, waist, left_leg, right_leg = 0, 0, 0, 0, 0
found = False
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            head_x = i
            head_y = j
            found = True
            break
    if found == True:
        break

heart_x, heart_y = head_x + 1, head_y

# 왼쪽 팔 길이
for j in range(heart_y - 1, -1, -1):
    if grid[heart_x][j] == '*':
        left_arm += 1
    if grid[heart_x][j] == '_':
        break

# 오른쪽 팔 길이
for j in range(heart_y + 1, n, 1):
    if grid[heart_x][j] == '*':
        right_arm += 1
    if grid[heart_x][j] == '_':
        break

# 허리 위치
for i in range(heart_x + 1, n, 1):
    if grid[i][heart_y] == '*':
        waist += 1
        waist_x = i
        waist_y = heart_y
    if grid[i][heart_y] == '_':
        break

# 왼쪽 다리 길이
for i in range(waist_x + 1, n, 1):
    if grid[i][waist_y - 1] == '*':
        left_leg += 1
    if grid[i][waist_y - 1] == '_':
        break

# 오른쪽 다리 길이
for i in range(waist_x + 1, n, 1):
    if grid[i][waist_y + 1] == '*':
        right_leg += 1
    if grid[i][waist_y + 1] == '_':
        break

print(heart_x + 1, heart_y + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
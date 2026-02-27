n, game = input().split()
n = int(n)

player = set()
cnt = 0
temp = 1

for _ in range(n):
    name = input()

    # 윷놀이 Y
    if game == "Y":
        if name not in player:
            player.add(name)
            temp += 1
        if temp == 2:
            cnt += 1
            temp = 1

    # 같은 그림 찾기 F
    elif game == "F":
        if name not in player:
            player.add(name)
            temp += 1
        if temp == 3:
            cnt += 1
            temp = 1

    # 원카드 O
    elif game == "O":
        if name not in player:
            player.add(name)
            temp += 1
        if temp == 4:
            cnt += 1
            temp = 1
print(cnt)
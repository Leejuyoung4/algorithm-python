n, game = input().split()
n = int(n)

player = set()

for _ in range(n):
    name = input()
    player.add(name)

# 윷놀이 Y
if game == "Y":
    print(len(player) // 1)

# 같은 그림 찾기 F
elif game == "F":
    print(len(player) // 2)

# 원카드 O
elif game == "O":
    print(len(player) // 3)
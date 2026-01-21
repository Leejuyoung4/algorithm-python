T = int(input())

for _ in range(T):
    score_Y = score_K = 0
    for i in range(9):
        Y, K = map(int, input().split())
        score_Y += Y
        score_K += K

    if score_Y == score_K:
        print("Draw")
    elif score_Y > score_K:
        print("Yonsei")
    elif score_Y < score_K:
        print("Korea")
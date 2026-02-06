N, K = map(int, input().split())

men = [0] * 7
women = [0] * 7

# 방 배정하기
for _ in range(N):
    S, Y = map(int, input().split())
    
    if S == 0:
        women[Y] += 1
    elif S == 1:
        men[Y] += 1

# 필요한 최소한의 방 개수 구하기
cnt = 0
for i in range(1, 7):
    cnt += (women[i] + K - 1) // K
    cnt += (men[i] + K - 1) // K

print(cnt)
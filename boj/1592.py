N, M, L = map(int, input().split())

cnt = 0
M_list = [0] * N

idx = 0
M_list[idx] = 1

while M_list[idx] != M:
    if M_list[idx] % 2 != 0:
        idx = (idx + L) % N
        cnt += 1
        M_list[idx] += 1

    elif M_list[idx] % 2 == 0:
        idx = (idx - L + N) % N
        cnt += 1
        M_list[idx] += 1

print(cnt)
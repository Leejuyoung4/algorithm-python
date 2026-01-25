T = int(input())

for _ in range(T):
    N = int(input())
    max_val = 0
    for _ in range(N):
        S, L = map(str, input().split())

        if int(L) > max_val:
            max_val = int(L)
            school = S

    print(school)
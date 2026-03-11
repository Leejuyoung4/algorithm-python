########## 방식 2 : 슬라이딩 윈도우
n, x = map(int, input().split())
visits = list(map(int, input().split()))

total = sum(visits[:x])
result = total
cnt = 1

for i in range(x, n):
    total += visits[i]
    total -= visits[i - x]

    if total == result:
        cnt += 1
    elif total > result:
        result = total
        cnt = 1

if result == 0:
    print('SAD')
else:
    print(result)
    print(cnt)


########## 방식 1 : 시간초과
# n, x = map(int, input().split())

# visits = list(map(int, input().split()))
# result = 0
# cnt = 0

# for idx in range(n - x + 1):
#     total = 0
#     for j in range(idx, idx + x):
#         total += visits[j]

#     if total == result:
#         cnt += 1
#     elif total > result:
#         result = total
#         cnt = 1

# if result == 0:
#     print('SAD')
# else:
#     print(result)
#     print(cnt)
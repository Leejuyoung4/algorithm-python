##### S - i 반복으로 S가 음수가 되는 순간에 멈추는 방식
S = int(input())
N = 0

for i in range(1, S + 1):
    S -= i

    if S < 0:
        break
    N += 1

print(N)




##### 누적합 방식
S = int(input())

total = 0
N = 0
i = 1

while total + i <= S:
    total += i
    N += 1
    i += 1

print(N)
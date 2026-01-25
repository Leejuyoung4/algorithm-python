##### 내장함수 사용

import math

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    print(math.lcm(A, B))



##### GCD(유클리드 호제법) 사용
T = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(T):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B) )
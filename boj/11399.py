N = int(input())
arr = list(map(int, input().split()))
arr.sort()

prefix = 0
time = 0
for i in arr:
    prefix += i
    time += prefix

print(time)
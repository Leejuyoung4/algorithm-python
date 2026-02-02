total = 0
arr = []

for _ in range(9):
    n = int(input())
    arr.append(n)
    total += n

a = b = -1
for i in range(0, len(arr) - 1):
    for j in range(i + 1, 9):
        if arr[i] + arr[j] == total - 100:
            a = i
            b = j
            break
    if a != -1:
        break

arr.pop(b)
arr.pop(a)
arr.sort()

for i in range(7):
    print(arr[i])
target = input()
idx = 0
num = 1

while idx < len(target):
    for ch in str(num):
        if idx < len(target) and target[idx] == ch:
            idx += 1
    num += 1

print(num - 1)
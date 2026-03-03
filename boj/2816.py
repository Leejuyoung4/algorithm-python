n = int(input())
channel = []
for _ in range(n):
    s = input()
    channel.append(s)

cursor = 0
result = ""

idx1 = channel.index("KBS1")

for _ in range(idx1):
    cursor += 1
    result += "1"

for _ in range(idx1):
    channel[cursor], channel[cursor - 1] = channel[cursor - 1], channel[cursor]
    cursor -= 1
    result += "4"

idx2 = channel.index("KBS2")

for _ in range(idx2):
    cursor += 1
    result += "1"

for _ in range(idx2 - 1):
    channel[cursor], channel[cursor - 1] = channel[cursor - 1], channel[cursor]
    cursor -= 1
    result += "4"

print(result)
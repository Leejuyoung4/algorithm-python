import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}

for _ in range(n):
    s = input().strip()
    if len(s) >= m:
        if s in words:
            words[s] += 1
        else:
            words[s] = 1

result = sorted(words.keys(), key=lambda x: (-words[x], -len(x), x))

for w in result:
    print(w)
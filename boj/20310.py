s = list(input())

cnt_0 = s.count('0') // 2
cnt_1 = s.count('1') // 2

# 1은 앞에서부터 제거
for i in range(len(s)):
    if cnt_1 > 0 and s[i] == '1':
        s[i] = ''
        cnt_1 -= 1

# 0은 뒤에서부터 제거
for i in range(len(s) - 1, -1, -1):
    if cnt_0 > 0 and s[i] == '0':
        s[i] = ''
        cnt_0 -= 1

for i in s:
    if i != '':
        print(i, end='')
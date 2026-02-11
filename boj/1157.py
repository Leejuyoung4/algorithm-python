s = input().upper()

dic = {}

for ch in s:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1

max_val = max(dic.values())

if list(dic.values()).count(max_val) > 1:
    print("?")
else:
    for key in dic:
        if dic[key] == max_val:
            print(key)
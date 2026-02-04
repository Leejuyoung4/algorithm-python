word = input()

i = 0
cnt = 0

while i < len(word):
    # dz=
    if i + 2 < len(word) and word[i] == 'd' and word[i+1] == 'z' and word[i+2] == '=':
        cnt += 1
        i += 3

    # c=, c-, s=, z=
    elif i + 1 < len(word) and word[i] in ('c', 's', 'z') and word[i+1] in ('=', '-'):
        cnt += 1
        i += 2

    # lj, nj
    elif i + 1 < len(word) and word[i] in ('l', 'n') and word[i+1] == 'j':
        cnt += 1
        i += 2

    # d-
    elif i + 1 < len(word) and word[i] == 'd' and word[i+1] == '-':
        cnt += 1
        i += 2

    else:
        cnt += 1
        i += 1

print(cnt)
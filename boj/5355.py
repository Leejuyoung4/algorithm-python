T = int(input())

for _ in range(T):
    math = list(map(str,input().split()))
    math[0] = float(math[0]) 

    for i in range(len(math)):
        if type(math[i]) == float:
            pass
        elif math[i] == '@':
            math[0] *= 3
        elif math[i] == '%':
            math[0] += 5
        elif math[i] == '#':
            math[0] -= 7
    print('%0.2f' % math[0])
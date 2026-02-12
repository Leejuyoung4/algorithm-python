import sys
input = sys.stdin.readline

s = set()
write = sys.stdout.write

m = int(input())
for _ in range(m):
    op = input().split()

    if len(op) >= 2:
        op[1] = int(op[1])
    
    if op[0] == 'add':
        s.add(op[1])

    elif op[0] == 'remove':
       s.discard(op[1])

    elif op[0] == 'check':
        if op[1] in s:
            write('1\n')
        else:
            write('0\n')
            
    elif op[0] == 'toggle':
        if op[1] in s:
            s.remove(op[1])
        else:
            s.add(op[1])

    elif op[0] == 'all':
        s = set(range(1, 21))

    elif op[0] == 'empty':
        s.clear()
s = input()
stack = []

i = 0
while i < len(s):
    if s[i] == '<':
        while stack:
            print(stack.pop(), end = "")
        
        while s[i] != '>':
            print(s[i], end = "")
            i += 1
        print('>', end = "")
        i += 1
    
    elif s[i] == ' ':
        while stack:
            print(stack.pop(), end = "")
        print(' ', end = "")
        i += 1
    
    else:
        stack.append(s[i])
        i += 1

while stack:
    print(stack.pop(), end = "")
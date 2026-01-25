T = int(input())

for _ in range(T):
    ch = input()
    status = 0
    score = 0

    for i in range(len(ch)):
        if ch[i] == "O":
            status += 1
            score += status
        else:
            status = 0
    
    print(score)
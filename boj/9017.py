t = int(input())
for _ in range(t):
    n = int(input())
    team = list(map(int, input().split()))

    temp = []
    for i in range(n):
        if team.count(team[i]) == 6:
            temp.append(team[i])

    num = 1
    cnt = [0] * (max(team) + 1)
    score = [0] * (max(team) + 1)
    fifth = [0] * (max(team) + 1)

    for i in range(len(temp)):
        if cnt[temp[i]] < 4:
            score[temp[i]] += num
            cnt[temp[i]] += 1
        
        elif cnt[temp[i]] == 4:
            fifth[temp[i]] = num
            cnt[temp[i]] += 1
            
        num += 1

    winner = min(temp, key = lambda x: (score[x], fifth[x]))
    print(winner)
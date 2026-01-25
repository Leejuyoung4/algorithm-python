T = int(input())

for _ in range(T):
    score = 0
    status = 1

    result = input()
    if result[0] == "O":
        score += 1

    for i in range(1, len(result)):
        if result[i] == "O":
            if result[i - 1] == "O":
                status += 1
                score += status
            else:
                score += 1
        elif result[i] == "X":
            status = 1
    print(score)
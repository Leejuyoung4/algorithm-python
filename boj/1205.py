n, score, p = map(int, input().split())
scores = []
if n > 0:
    scores = list(map(int, input().split()))

rank = 1

if n == 0:
    if p == 0:
        print(-1)
    else:
        print(1)

else:
    if n < p:
        scores.append(score)
        scores.sort()
        for s in scores:
            if score > s:
                rank += 1
        print(rank)

    else:
        if score > min(scores):
            scores.pop(scores.index(min(scores)))
            scores.append(score)
            scores.sort(reverse = True)
            for s in scores:
                if s > score:
                    rank += 1
            print(rank)

        elif score <= min(scores):
            print(-1)
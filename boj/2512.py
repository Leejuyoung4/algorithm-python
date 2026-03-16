############### 이분탐색

n = int(input())
region = list(map(int, input().split()))
m = int(input())

if sum(region) <= m:
    print(max(region))
else:
    left = 0
    right = max(region)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        total = 0

        for r in region:
            total += min(r, mid)

        if total <= m:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)
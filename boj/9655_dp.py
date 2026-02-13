n = int(input())

dp = [False] * (n + 1)

if n >= 1:
    dp[1] = True

if n >= 2:
    dp[2] = False

if n >= 3:
    dp[3] = True

for i in range(4, n + 1):
    take1 = False
    if dp[i - 1] == False:
        take1 = True
    
    take3 = False
    if dp[i - 1] == False:
        take3 = True

    if take1 == True or take3 == True:
        dp[i] = True
    else:
        dp[i] = False

if dp[n] == True:
    print('SK')
else:
    print('CY')
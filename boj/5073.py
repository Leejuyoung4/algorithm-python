while True:
    # 세 변의 길이 입력 및 정렬
    num = list(map(int, input().split()))
    num.sort()

    i = 0
    if num[i] == num[i + 1] == num[i + 2] == 0:
        break
    elif num[i] == num[i + 1] == num[i + 2]:
        print('Equilateral')
    elif num[i] + num[i + 1] > num[i + 2]:
        if num[i] == num[i + 1] or num[i + 1] == num[i + 2] or num[i + 2] == num[i]:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')
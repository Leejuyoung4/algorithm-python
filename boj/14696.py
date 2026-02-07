N = int(input())

for _ in range(N):
    cnt_a = [0] * 5
    cnt_b = [0] * 5

    # A 입력
    data = list(map(int, input().split()))
    arr = data[1:]

    for i in range(len(arr)):
        idx = arr[i]
        cnt_a[idx] += 1

    # B 입력    
    data = list(map(int, input().split()))
    arr = data[1:]
    
    for i in range(len(arr)):
        idx = arr[i]
        cnt_b[idx] += 1

    # 결과 출력        
    for i in range(4, 0, -1):
        if cnt_a[i] > cnt_b[i]:
            print('A')
            break
        elif cnt_b[i] > cnt_a[i]:
            print('B')
            break
    else:
        print('D')
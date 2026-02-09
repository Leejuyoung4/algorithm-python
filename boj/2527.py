for _ in range(4):
    # 입력값
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # d : 공통부분이 없음
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')
    
    # c : 점
    elif (p1 == x2 or x1 == p2) and (q1 == y2 or y1 == q2):
        print('c')
    
    # b : 선
    elif (p1 == x2) or (x1 == p2) or (q1 == y2) or (y1 == q2):
        print('b')
    
    # a : 직사각형
    else:
        print('a')
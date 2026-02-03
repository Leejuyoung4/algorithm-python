arr = set()
for _ in range(10):
    n = int(input())

    # 42로 나눈 나머지
    arr.add(n % 42)

print(len(arr))
K = int(input())

edges = []
for _ in range(6):
    d, l = map(int, input().split())
    edges.append([d, l])

max_width = max_height = 0
max_width_idx = max_height_idx = 0

for i in range(len(edges)):
    d = edges[i][0]
    l = edges[i][1]

    if d == 1 or d == 2:
        if l > max_width:
            max_width = l
            max_width_idx = i
        
    if d == 3 or d == 4:
        if l > max_height:
            max_height = l
            max_height_idx = i
    
whole = max_width * max_height
part = (abs(edges[(max_width_idx - 1) % 6][1] - edges[(max_width_idx + 1) % 6][1])) * (abs(edges[(max_height_idx - 1) % 6][1] - edges[(max_height_idx + 1) % 6][1]))

print((whole - part) * K)
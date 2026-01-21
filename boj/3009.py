list_x, list_y= [], []

for i in range(3):
    x, y = map(int, input().split())

    list_x.append(x)
    list_y.append(y)

for i in range(3):
    if list_x.count(list_x[i]) == 1:
        x_d = list_x[i]
    if list_y.count(list_y[i]) == 1:
        y_d = list_y[i]

print(x_d, y_d)
# сортировка вставками
a = [-2, 3, 0, 0, -5, 3, 21, 25]
n = len(a)
for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
print(a)


# слияние двух списков

a = [1, 4, 10, 11]
b = [2, 3, 3, 4, 8]
c = []

n = len(a)
m = len(b)

i = 0
j = 0
while i < n and j < m:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c += a[i:] + b[j:]

#
# if i < n:
#     for k in range(i, n):
#         c.append(a[k])
# elif j < m:
#     for k in range(j, m):
#         c.append(b[k])
print(c)
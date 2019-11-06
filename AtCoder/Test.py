l = [0, 1, 2, 3, 4, 5]
a = [6, 7, 8, 9, 10, 11]
for i in range(6):
    a[i] = max(a[i], a[i]+1)
print(a)
n, y = map(int, input().split())
n_1000 = 0
n_5000 = 0
n_10000 = 0
key = 0
for i in range(n+1):
    for j in range(n+1-i):
        total = 1000*i + 5000*j + 10000*(n-i-j)
        if total == y:
            key = 1
            n_1000 = i
            n_5000 = j
            break
        else:
            continue
if key == 1:
    print(n-n_1000-n_5000, n_5000, n_1000, sep=' ')
else:
    print(('-1 -1 -1'))
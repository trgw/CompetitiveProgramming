n, m = map(int, input().split())
lli = []
lri = []
for i in range(1, m+1):
    li, ri = map(int, input().split())
    lli.append(li)
    lri.append(ri)
lans = []
for i in range(1, n+1):
    lans.append(i)
for i in range(m):
    for j in range(1, n+1):
        if not lri[i] <= j <= lri[i]:
            lans.remove(j)
print(len(lans))
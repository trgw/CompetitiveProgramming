n, x = map(int, input().split())
l =list(map(int, input().split()))
d = [0]
for i in range(n): #range(n+1)とミス
    d.append(d[i]+l[i])
ans = 0
for i in range(n+1):
    if d[i] <= x:
        ans += 1
print(ans)
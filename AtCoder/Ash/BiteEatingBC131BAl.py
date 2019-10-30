n, l = map(int, input().split())
la = [l+i for i in range(n)]
ans = sum(la)
if l+n-1 < 0:
    ans -= l+n-1
elif 0 < l:
    ans -= l
print(ans)
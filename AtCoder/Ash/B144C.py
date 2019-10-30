'''
TLE
n = int(input())
l = []
for i in range(2,n):
    for j in range(2,n):
        l.append(i*j)
if n not in l:
    ans = n-1
else:
    lf = []
    for k in range(1, n+1):
        if n % k == 0:
            lf.append(k)
        i = lf[len(lf) // 2 - 1]
        j = lf[len(lf) // 2]
        ans = i + j - 2
print(ans)
'''

'''
n = int(input())
l = []
m = n**0.5
q = m // 1
r = int(q)
ans = 0
i = 0
j = 0
for i in range(2,r+1):
    for j in range(2,r+1):
        l.append(i*j)
    l.append(n)
    if n not in l:
        ans = n-1
    else:
        lf = []
        for k in range(1, r+1):
            if n % k == 0:
                lf.append(k)
        
        lf.append(n)
        i = lf[len(lf) // 2 - 1]
        j = lf[len(lf) // 2]
        ans = i + j - 2
print(i)
print(j)
print(ans)
'''

# (1, 1) から (a, b) に至るまでの移動回数は a + b − 2 です。
# したがって問題は、「a × b = N となるような (a, b) について、a + b − 2 の最小値を求めよ」となります。
# 対称性から a ≤ b としてよいので、a ≤√N までを全探索することにより O(√N) で解くことができます。
n = int(input())
ln = []
for k in range(1,(int(n**0.5))+1):
    if n % k == 0:
        ln.append(k)
if not n**0.5 % 1 == 0:
    for k in reversed(range(0, len(ln))):
        ln.append(n // ln[k])
else:
    for k in reversed(range(0, len(ln)-1)):
        ln.append(n // ln[k])
if not n**0.5 % 1 == 0:
    i = ln[len(ln) // 2 - 1]
    j = ln[len(ln) // 2]
    ans = i + j -2
else:
    ans = int(2*n**0.5)-2
print(ans)
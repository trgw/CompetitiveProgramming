'''
n = int(input())
sp ={}
S = []
P = []
for _ in range(n):
    s, p = input().split()
    S.append(s)
    P.append(p)
for i in range(n):
    sp['S[i]'] = P[i]
print(sp)
print(S)
print(P)
'''

# from operator import itemgetter
# from operator import attrgetter
n = int(input())
isp = []
S = []
P = []
for _ in range(n):
    s, p = input().split()
    p = int(p)
    S.append(s)
    P.append(p)
for i in range(n):
    isp.append([i+1, S[i], P[i]])
isp = sorted(isp, key=lambda x: x[2], reverse=True)
isp = sorted(isp, key=lambda x: x[1])
for i in range(n):
    print(isp[i][0])


'''
n = int(input())
la = list(map(int, input().split()))
ld = []
for j in range(1, n):
    ld.append(abs(sum(la[0:j+1])-sum(la[j+1:n])))
print(min(ld))
# print(ld)
# print(ld.index(min(ld)))
'''

'''
TLE

n = int(input())
la = list(map(int, input().split()))
ld = [abs(sum(la[0:j+1])-sum(la[j+1:n])) for j in range(1, n)]
if n == 2:
    print(abs(la[0] - la[1]))
else:
    print(min(ld))
'''

n = int(input())
la = list(map(int, input().split()))
tmp = 0
ind = 0
for i in range(n):
    tmp += la[i]
    if 2*tmp >= sum(la):
        ind = i
        break
if n == 2:
    ans = abs(la[0]-la[1])
else:
    ans = abs(tmp - (sum(la)-tmp))
print(tmp)
print(ind)
print(ans)
'''
#import pprint
n, d = map(int, input().split())
#x = list[int(input().split()) for i range(1, n+1)]
x = [list(map(int, input().split())) for _ in range(1, n+1)]
#pprint.pprint(x)

cnt = 0
a = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        for k in range(1, d+1):
            a += (x[i][k]-x[j][k])**2
        if (a**0.5)%1 == 0:
            cnt += 1
print(cnt)
'''

#import pprint
n, d = map(int, input().split())
#x = list[int(input().split()) for i range(1, n+1)]
x = [list(map(int, input().split())) for _ in range(n)]
#pprint.pprint(x)

cnt = 0
a = 0
for i in range(n-1):
    for j in range(i+1, n):
        for k in range(d):
            a += (x[i][k]-x[j][k])**2
        if (a**0.5)%1 == 0:
            cnt += 1
            a = 0
print(cnt)
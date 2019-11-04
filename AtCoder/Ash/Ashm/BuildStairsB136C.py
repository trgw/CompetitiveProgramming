'''
n = int(input())
h = list(map(int, input().split()))
for i in range(n-1):
    if h[i+1] == h[i] - 1:
        h[i] = h[i] - 1
flag = True
for i in range(n-1):
    if h[i+1] < h[i]:
        flag = False
        break
if flag == True:
    print('Yes')
else:
    print('No')

5
2 2 2 2 1
などに対応できていない
'''

n = int(input())
h = list(map(int, input().split()))
for i in reversed(range(n-1)):
    if h[i+1] == h[i] - 1:
        h[i] = h[i] - 1
flag = True
for i in range(n-1):
    if h[i+1] < h[i]:
        flag = False
        break
if flag == True:
    print('Yes')
else:
    print('No')
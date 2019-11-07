'''ls = list(input())
n = len(ls) + 1
nm = ls.count('<')
np = ls.count('>')
la = [len(ls)]
for i in range(n-1):
    if ls[i] == '<':
        la.append(la[i]+1)
    else:
        la.append(la[i]-1)
print(la)
print(sum(la) - n*min(la))
print(sum(la))
print(n*min(la))'''

'''ls = list(input())
n = len(ls) + 1
la = [len(ls)]
for i in range(n-1):
    if ls[i] == '<' and ls[i+1] == '<':
        la.append(la[i]+1)
    elif ls[i] == '<' and ls[i+1] == '>':'''

'''

TLE

s = input()
n = len(s) + 1
lft = 0
rgt = 0
l = []
for i in range(n):
    for j in reversed(range(i)):
        if s[j] == '<':
            lft += 1
        else:
            break
    for j in range(i, n-1):
        if s[j] == '>':
            rgt += 1
        else:
            break
    l.append(max(lft, rgt))
    lft = 0
    rgt = 0
print(sum(l))'''

s = input()
n = len(s) + 1
a = [0 for _ in range(n)]
for i in range(n-1):
    if s[i] == '<':
        a[i+1] = a[i] + 1
for i in reversed(range(1, n)):
    if s[i-1] == '>':
        a[i-1] = max(a[i-1], a[i]+1)
print(sum(a))
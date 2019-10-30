'''
test2
# TLE
n = int(input())
s = []
for _ in range(n):
    s.append(''.join(sorted(input())))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            ans += 1
print(ans)
'''

n = int(input())
s = []
for _ in range(n):
    s.append(''.join(sorted(input())))
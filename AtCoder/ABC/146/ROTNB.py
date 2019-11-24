n = int(input())
s = input()
ls = list(s)
la = [chr(i) for i in range(65, 65+26)]
lind = []
for i in range(len(s)):
    for j in range(len(la)):
        if ls[i] == la[j]:
            lind.append(la.index(la[j]))
            break
lans = [la[lind[i]-26+n] for i in range(len(s))]
ans = ''.join(lans)
print(ans)
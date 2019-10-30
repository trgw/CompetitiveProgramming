# O(√n)enumerate_factors
n = int(input())
ln = []
for i in range(1,(int(n**0.5))+1):
    if n % i == 0:
        ln.append(i)
if not (n**0.5) % 1 == 0:
    for i in reversed(range(0, len(ln))):
        ln.append(n // ln[i])
else:
    for i in reversed(range(0, len(ln)-1)):
        ln.append(n // ln[i])
print(ln)
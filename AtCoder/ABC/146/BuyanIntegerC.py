a, b, x = map(int, input().split())
nn = x//a
s = str(nn)
d = 0
if x % a != 0:
    d = len(s)
else:
    d = len(s) - 1
anbd = a*nn + b*d
n = (x-b*d)//a
#  print(nn)
#  print(d)
ans = 0
if n >= 1000000000:
    print(1000000000)
elif b > 10*a:
    print(int(((x-b*d)/a)//1))
elif x < anbd:
    print(0)
else:
    print(n)
#  print((x-b*d)/a)
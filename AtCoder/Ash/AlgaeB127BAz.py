r, d, x2000 = map(int, input().split())
x2001to2010 = [r*x2000-d]
for i in range(10):
    x2001to2010.append(r*x2001to2010[i]-d)
for i in range(10):
    print(x2001to2010[i])
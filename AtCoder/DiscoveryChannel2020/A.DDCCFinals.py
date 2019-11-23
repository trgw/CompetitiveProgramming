x, y = map(int, input().split())
if x == 1 and y == 1:
    print(300000*2 + 400000)
elif x == 1 and y == 2:
    print(300000+200000)
elif x == 1 and y == 3:
    print(300000+100000)
elif x == 2 and y == 1:
    print(300000 + 200000)
elif x == 2 and y == 2:
    print(200000+200000)
elif x == 2 and y == 3:
    print(200000+100000)
elif x == 3 and y == 1:
    print(100000+300000)
elif x == 3 and y == 2:
    print(100000+200000)
elif x == 3 and y == 3:
    print(100000+100000)
elif x == 1:
    print(300000)
elif x == 2:
    print(200000)
elif x == 3:
    print(100000)
elif y == 1:
    print(300000)
elif y == 2:
    print(200000)
elif y == 3:
    print(100000)
else:
    print(0)
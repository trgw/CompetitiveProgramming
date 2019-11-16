n = int(input())
s = input()
ls = list(s)
l1 = []
l2 = []
if n % 2 == 1:
    print('No')
else:
    for i in range(len(s)//2):
        l1.append(ls[i])
    for i in (range(len(s)//2, n)):
        l2.append(ls[i])
    if l1 == l2:
        print(('Yes'))
    else:
        print('No')
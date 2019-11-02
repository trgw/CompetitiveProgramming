da, db = map(int, input().split())
if db == da:
    l = [str(10*da), str(10*da+1)]
    print(' '.join(l))
elif db == da + 1:
    l = [str(10*da+9), str(10*db)]
    print(' '.join(l))
elif da == 9 and db == 1:
    print('9 10')
else:
    print(-1)
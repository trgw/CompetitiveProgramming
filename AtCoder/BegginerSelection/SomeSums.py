n, a, b = map(int, input().split())
ns = str(n)
lns = list(ns)
lni = [int(i) for i in lns]  # 数値の文字列のリスト➝数値のリスト はリスト内包表記
cnt = 0
for i in range(1, n+1):
    ist = str(i)
    lis = list(ist)
    lii = [int(j) for j in lis]
    if a <= sum(lii) <= b:
        cnt += i
#  print(lns)
#  print(lni)
print(cnt)
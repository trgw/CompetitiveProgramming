'''
n = int(input())
a = map(int, input().split())
# a = int(input().split()) ・・・Unionでないとダメ
# print(a) <map object at 0x00000229A2CA3C08>
la = list(a)
# la2 = [la[i]/2 for i in la] ・・・✖
cnt = 0
while True:  # ：無限ループ➝どこかでbreakしなければならない
    for i in range(n):
        if la[i] % 2 == 0:
            la[i] /= 2  # !!
        else:
            cnt -= 1
            break
    cnt += 1
    break
print(cnt)
WA
'''

n = int(input())
a = map(int, input().split())
la = list(a)
flag = True
cnt = 0
while flag:
    for i in range(n):
        if la[i] % 2 == 0:
            la[i] /= 2  # !!
        else:
            flag = False
            cnt -= 1
            break
    cnt += 1
print(cnt)
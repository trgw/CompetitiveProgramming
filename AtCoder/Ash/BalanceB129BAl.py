n = int(input())
w = list(map(int, input().split()))
S1 = []
S2 = []
for t in range(n):
    S1.append(sum(w[0:t+1]))
    S2.append(sum(w[t+1:n]))
av = []
for i in range(n):
    av.append(abs(S1[i]-S2[i]))
#print(S1)
#print(S2)
#print(av)
print(min(av))
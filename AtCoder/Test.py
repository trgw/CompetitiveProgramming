import math
import itertools
N = int(input())
l = [list(map(int, input().split())) for i in range(N)]
def root(xi, yi, xj, yj):
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

m = 0
for i in itertools.permutations(l, len(l)):
    k = 0
    for j in range(len(i)-1):
        k += root(*(i[j] + i[j+1]))
    m += k
print(m/math.factorial(len(l)))

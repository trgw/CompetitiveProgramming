import numpy as np
n, m, b = 40, 100, 300
gx, gy = map(int, input().split())
#  for i in range(m):
#      ry
r = np.array([input().split() for _ in range(m)])
b = np.array([list(map(int,input().split())) for _ in range(b)])
a, b, c, x, y = map(int, input().split())
if a + b >= 2*c and x <= y and (2*c*x + b*(y-x)) >= 2*c*y:
    print(2*c*y)
elif a + b >= 2 * c and x <= y and (2 * c * x + b * (y - x)) < 2 * c * y:
    print(2 * c * x + b * (y - x))
elif a + b >= 2*c and x > y and (2*c*y + a*(x-y)) >= 2*c*x:
    print(2*c*x)
elif a + b >= 2 * c and x > y and (2 * c * y + a * (x - y)) < 2 * c * x:
    print(2*c*y + a*(x-y))
elif a + b < 2*c:
    print(a*x + b*y)
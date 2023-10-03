from math import sqrt

x, y, R = map(float, input().split())

if 0 <= x <= 2*R and 0 <= y <= -R:
    print('yes')
else:
    y1 = R - sqrt(R ** 2 - (x + R) ** 2)
    y2 = R + sqrt(R ** 2 - (x + R) ** 2)
    if y1 <= y <= y2:
        print('yes')
    else:
        print('no')

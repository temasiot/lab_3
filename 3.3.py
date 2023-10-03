from math import sqrt

x, R = map(float, input().split())

if x <= -R:
    y = R
elif -R < x < R:
    y = R-sqrt(R**2-x**2)
elif R <= x < 6:
    y = (9*R-3*x-R*x)/(6-R)
else:
    y = x-9
print(y)

a, b, c, x = map(float, input().split())
if x < 5 and c != 0:
    F = -a*x**2-b
elif x > 5 and c == 0:
    F = (x-a)/x
else:
    F = -x/c
print(F)

if x < 5 and c != 0:
    F = -a*x**2-b
if x > 5 and c == 0:
    F = (x-a)/x
if not(x < 5 and c != 0) and not(x > 5 and c == 0):
    F = -x/c
print(F)

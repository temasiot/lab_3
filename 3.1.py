from math import log10
from math import e
from math import atan

x = float(input())
y = abs(9*x**3+2)

if x < 4:
    y += 3*x**5-x**3+2*x-1
if x >= 7:
    y += log10(2*x**(-1) + e**(3*x+1))
if 4 <= x < 7:
    y += atan((x-2)/3)
print(y)

y = abs(9*x**3+2)
if x < 4:
    y += 3*x**5-x**3+2*x-1
elif x >= 7:
    y += log10(2*x**(-1) + e**(3*x+1))
else:
    y += atan((x-2)/3)
print(y)

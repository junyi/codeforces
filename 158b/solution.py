import math
from collections import Counter
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split())

count = 0
if n == 1:
    count = 1
else:
    c = Counter(ar)
    count += c[4]

    two = c[2]/2
    count += two
    c[2] -= two * 2

    common = min(c[3], c[1])
    count += common
    c[3] -= common
    c[1] -= common

    if c[3] != 0:
        count += c[3]
    elif c[1] != 0:
        if c[2] == 1:
            count += 1
            c[2] -= 1
            c[1] -= min(2, c[1])
        count += int(math.ceil(c[1]/4.0))

    count += c[2]

print count

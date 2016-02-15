j = 0
i = 0
for x in xrange(5):
    ar = map(int, raw_input().strip().split())
    if 1 in ar:
        j = ar.index(1)
        i = x

print abs(i - 2) + abs(j - 2)

import sys
n, t = map(int, raw_input().strip().split())
s = raw_input().strip()
d = []
for i, x in enumerate(s):
    if x == 'B':
        d.append(i)

l = len(d)
for _ in xrange(1, t + 1):
    for i, x in enumerate(d):
        if i < l - 1:
            if x + 1 < d[i + 1]:
                d[i] = min(n - 1, x + 1)
        else:
            d[i] = min(n - 1, x + 1)

index = 0
for i in xrange(n):
    if len(d) > index and i == d[index]:
        sys.stdout.write('B')
        index += 1
    else:
        sys.stdout.write('G')
print

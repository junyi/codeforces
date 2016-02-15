n = int(raw_input().strip())
ar = map(int, raw_input().strip().split())
d = {}
for i, x in enumerate(ar):
    d[x] = str(i + 1)

print ' '.join(d[i] for i in xrange(1, n + 1))

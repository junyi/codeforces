n = int(raw_input().strip())
count = 0
for _ in xrange(n):
    p, q = map(int, raw_input().strip().split())
    if q - p >= 2:
        count += 1
print count

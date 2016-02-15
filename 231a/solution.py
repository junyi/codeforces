n = int(raw_input().strip())
count = 0
for _ in xrange(n):
    ar = map(int, raw_input().strip().split())
    if sum(ar) >= 2:
        count += 1
print count

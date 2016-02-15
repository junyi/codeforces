n = int(raw_input().strip())
total = 0
capacity = 0
for _ in xrange(n):
    a, b = map(int, raw_input().strip().split())
    total += b - a
    capacity = max(capacity, total)
print capacity

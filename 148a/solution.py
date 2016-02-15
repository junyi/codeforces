k = int(raw_input().strip())
l = int(raw_input().strip())
m = int(raw_input().strip())
n = int(raw_input().strip())
d = int(raw_input().strip())

count = 0
l = [k, l, m, n]
for i in xrange(1, d + 1):
    if any([i % x == 0 for x in l]):
        count += 1
print count

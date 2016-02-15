n, m = map(int, raw_input().strip().split())
ar = map(int, raw_input().strip().split())
ar = sorted(ar)
diff = ar[n - 1] - ar[0]
for i in xrange(1, m - n + 1):
    alt = ar[i + n - 1] - ar[i]
    diff = min(diff, alt)
print diff

import math

n, m, a = map(int, raw_input().strip().split())
print int(math.ceil(n/float(a)) * math.ceil(m/float(a)))

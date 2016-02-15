import math
def is_composite(n):
    if n < 2:
        return False
    r = int(math.sqrt(n))
    for i in xrange(2, r + 1):
        if n % i == 0:
            return True
    return False

n = int(raw_input().strip())
a = n/2
b = n - a

while True:
    if is_composite(a) and is_composite(b):
        print a, b
        break
    a += 1
    b -= 1

from fractions import gcd
a, b, n = map(int, raw_input().strip().split())
turn = True # Simon
while True:
    qty = gcd(a if turn else b, n)
    if n >= qty:
        n -= qty
    else:
        break
    turn = not turn
print 1 if turn else 0

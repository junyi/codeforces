def candles(a, b):
    if b > a:
        return a

    total = 0
    n = a
    r = 0
    while n > 0:
        amount = n
        total += amount
        next_amount = n/b
        remainder = n % b
        n += next_amount + (r + remainder) / b
        r = (r + remainder) % b
        n -= amount
    return total

a, b = map(int, raw_input().strip().split())
print candles(a, b)

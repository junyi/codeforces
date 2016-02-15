m, n = map(int, raw_input().strip().split())

num = 0
if n % 2 == 0:
    num = n/2 * m
elif m % 2 == 0:
    num = m/2 * n
elif n > 1 or m > 1:
    num = m * n / 2
print num

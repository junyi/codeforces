n = int(raw_input().strip())
value = 0
for _ in xrange(n):
    s = raw_input().strip()
    if s == 'X++' or s == '++X':
        value += 1
    elif s == 'X--' or s == '--X':
        value -= 1
print value

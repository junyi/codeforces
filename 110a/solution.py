from collections import Counter

def is_lucky(num):
    return set(str(num)).issubset(set('47'))

n = raw_input().strip()
c = Counter(n)
if '4' in c or '7' in c:
    total = 0
    if '4' in c:
        total += c['4']
    if '7' in c:
        total += c['7']
    print 'YES' if is_lucky(total) else 'NO'
else:
    print 'NO'

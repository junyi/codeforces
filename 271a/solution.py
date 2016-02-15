from collections import Counter
def is_distinct(num):
    c = Counter(str(num))
    return c.most_common(1)[0][1] == 1

n = int(raw_input().strip())

found = False
while not found:
    n += 1
    found = is_distinct(n)
print n

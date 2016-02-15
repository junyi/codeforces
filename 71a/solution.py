def abbrev(word):
    l = len(word)
    if l <= 10:
        return word

    return word[0] + str(l - 2) + word[-1]

n = int(raw_input().strip())
for _ in xrange(n):
    s = raw_input().strip()
    print abbrev(s)

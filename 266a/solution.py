n = int(raw_input().strip())
s = raw_input().strip()

total = 0
index = 0
for i in xrange(1, n):
    if s[i] == s[index]:
        total += 1
    else:
        index = i
print total

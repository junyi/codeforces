s1 = raw_input().strip().lower()
s2 = raw_input().strip().lower()
l = len(s1)
diff = 0
for i in xrange(l):
    if s1[i] > s2[i]:
        diff = 1
        break
    elif s1[i] < s2[i]:
        diff = -1
        break
print diff

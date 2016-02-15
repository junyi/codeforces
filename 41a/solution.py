s1 = raw_input().strip()
s2 = raw_input().strip()
l1 = len(s1)
l2 = len(s2)
if l1 != l2:
    print 'NO'
else:
    same = all([s1[i] == s2[l1 - i - 1] for i in xrange(l1)])
    print 'YES' if same else 'NO'

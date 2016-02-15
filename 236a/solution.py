s = raw_input().strip()
size = len(set(s))
print 'CHAT WITH HER!' if size % 2 == 0 else 'IGNORE HIM!'

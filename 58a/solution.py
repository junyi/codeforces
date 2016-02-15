s = raw_input().strip()
hello = 'hello'
pos = 0

for i in s:
    if pos < 5 and i == hello[pos]:
        pos += 1

print 'YES' if pos == 5 else 'NO'

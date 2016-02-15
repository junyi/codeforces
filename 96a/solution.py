s = raw_input().strip()

counter = 1
prev = s[0]
found = False
for i in s[1:]:
    if i == prev:
        counter += 1
        if counter >= 7:
            found = True
            break
    else:
        counter = 1
    prev = i
print 'YES' if found else 'NO'

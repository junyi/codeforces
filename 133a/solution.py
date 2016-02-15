s = raw_input().strip()

output = False
for i in s:
    if i == 'H' or i == 'Q' or i == '9':
        output = True
        break
print 'YES' if output else 'NO'

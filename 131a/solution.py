s = raw_input().strip()
uppercase = all([i.isupper() for i in s[1:]])
if uppercase:
    print s[0].swapcase() + s[1:].lower()
else:
    print s

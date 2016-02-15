s = raw_input().strip()
result = []
vowels = set('aoyeui')
for c in s:
    cl = c.lower()
    if cl not in vowels:
        result.append('.')
        result.append(cl)
print ''.join(result)

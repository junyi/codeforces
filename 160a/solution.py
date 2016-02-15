n = int(raw_input().strip())
ar = map(int, raw_input().strip().split())
c = dict()
total = 0
for i in ar:
    if i not in c:
        c[i] = 0
    c[i] += 1
    total += i

coins = sorted(c.keys(), reverse=True)

current_total = 0
num_coins = 0
for e in coins:
    while c[e] > 0:
        if current_total <= total:
            total -= e
            current_total += e
            c[e] -= 1
            num_coins += 1
        else:
            break
print num_coins

n, k = map(int, raw_input().strip().split())
ar = map(int, raw_input().strip().split())

count = 0
benchmark = 0
for i, score in enumerate(ar):
    if i + 1 <= k or score == benchmark:
        if i == k - 1:
            benchmark = score
        if score > 0:
            count += 1
        else:
            break
    else:
        break
print count

import math
names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
n = int(raw_input().strip())
d, r = n/5, n % 5
x = int(math.log(d + 1)/math.log(2))
p = pow(2, x)
index = ((d - p + 1) * 5 + r - 1) / p
print names[index]

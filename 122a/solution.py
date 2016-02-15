def hard_lucky(num):
    if num < 47:
        return
    current = None
    cur_list = []
    length = 2
    prev_list = ['47']
    while not current or current < num:
        if not current:
            current = 47
            yield current
        else:
            for i in prev_list:
                for k in xrange(length - 1, -1, -1):
                    for j in ['4', '7']:
                        temp = i[:k] + j + i[k:]
                        temp_num = int(temp)
                        if temp_num > num:
                            return
                        if len(cur_list) > 0 and temp_num <= int(cur_list[-1]):
                            continue
                        cur_list.append(temp)
                        current = temp_num
                        yield current
            length += 1
            prev_list = cur_list
            cur_list = []

def is_lucky(num):
    if set(str(num)).issubset(set('47')):
        return True
    if num % 4 == 0 or num % 7 == 0:
        return True
    factors = hard_lucky(num)
    for i in factors:
        if num % i == 0:
            return True
    return False

n = int(raw_input().strip())

print 'YES' if is_lucky(n) else 'NO'

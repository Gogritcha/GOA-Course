def filter_list(l):
    filterd_list = []
    for i in l:
        if type(i) == int:
            filterd_list.append(i)
    return filterd_list


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
        

def digital_root(n):
    if len(str(n)) != 1:
        while len(str(n)) != 1:
            a = 0
            for i in str(n):
                a += int(i)
            n = a
        return a
    else:
        return n
# part1 q3
def bisect(lst, ele):
    # concat lst and ele
    buf = sorted(lst + [ele])
    # then always find a the ele in list
    min = 0
    max = len(buf) - 1
    while True:
        mid = (min + max) / 2
        if buf[mid] < ele:
            min = mid + 1
        elif buf[mid] > ele:
            max = mid - 1
        else:
            return mid

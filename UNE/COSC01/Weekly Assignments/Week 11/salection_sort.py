def index_smallest(l, lower, upper):
    min_index = lower
    for i in range(lower + 1, upper):
        if l[i] < l[min_index]:
            min_index = i
    return min_index
def selectionsort(l):
    for i in range(len(l)):
    j = index_smallest(l, i, len(l))
    l[i], l[j] = l[j], l[i]
    return l
def msort(l, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l[k] = left[i]
            i = i + 1
        else:
            l[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        l[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        l[k] = right[j]
        j = j + 1
        k = k + 1
    return l






def mergesort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        mergesort(left)
        mergesort(right)
        msort(l, left, right)
    return l

data = [2, 6, 3, 8, 4, 1, 100, 7, 101]
print(mergesort(data[:]))
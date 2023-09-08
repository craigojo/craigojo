def pivot(l, a, b):
    p = l[(a + b)//2]
    i, j = a - 1, b + 1
    while True:
        i, j = i + 1, j - 1
        while l[i] < p: i = i + 1
        while l[j] > p: j = j - 1
        if i >= j: return j
        l[i], l[j] = l[j], l[i]


def quicksort(l, a, b):
    if a < b:
        p = pivot(l, a, b)
        quicksort(l, a, p)
        quicksort(l, p + 1, b)
        return l
    

def qs(l):
    return quicksort(l, 0, len(l) - 1)


data = [1, 4 ,6 ,0 ,2 ,3, 9, 8, 4]
sorted_data = qs(data[:])
print(sorted_data)
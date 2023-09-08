def pivot(l, a, b): 
    p = l[(a + b)//2]
    i, j = a - 1, b + 1
    while True:
        i, j = i + 1, j - 1
        while l[i] < p:
            i = i + 1
        while l[j] > p:
            j = j - 1
        if i >= j: 
            return j

        l[i], l[j] = l[j], l[i]

def qs(l, a, b):
    if a < b:
        p = pivot(l, a, b)
        qs(l, a, p)
        qs(l, p + 1, b)
    return l
def quicksort(l):
    return qs(l, 0, len(l) - 1)


data = [2, 6, 3, 8, 4, 1, 100, 7, 101]
print(quicksort(data[:]))
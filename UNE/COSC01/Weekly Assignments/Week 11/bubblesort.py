def bubblesort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l



data = [2, 6, 3, 8, 4, 1, 100, 7, 101]
print(bubblesort(data[:]))
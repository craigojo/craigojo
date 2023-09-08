def insertionsort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j - 1], l[j] = l[j], l[j - 1]
            j = j - 1
    return l

data = [2, 6, 3, 8, 4, 1, 100, 7, 101]
print(insertionsort(data[:]))
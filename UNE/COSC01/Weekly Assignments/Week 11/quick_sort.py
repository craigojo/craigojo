# def index_smallest(l, lower, upper):
#     min_index = lower
#     for i in range(lower + 1, upper + 1):
#         if l[i] < l[min_index]:
#             min_index = i
#     return min_index



# def selectionsort(l):
#     for i in range(len(l) - 1):
#         j = index_smallest(l, i, len(l) - 1)
#         l[i], l[j] = l[j], l[i]
#     return l


# data = [1, 4 ,6 ,0 ,2 ,3, 9, 8, 4]
# print(selectionsort(data[:]))


# Put this into pythontutor and learn





# Run this selection on its own with the following list
# The result is 4, 4 is the index value of the smallest number in the list
# l = list

l = [1, 4, 2, 9, 0, 3]

# def index_smallest(l, lower, upper):
#     min_index = lower
#     for i in range(lower + 1, upper + 1):
#         if l[i] < l[min_index]:
#             min_index = i
#     return min_index

print(index_smallest(l, 0, len(l) - 1))
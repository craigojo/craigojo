list_1 = ['a', 'c', 'b', 'b2', 'd', 'f', '1g', 'h', 'i']
list_2 = ['e4', 'z', 'a', 'c', 'd', 'code', 'e', 'e2', 'f', 'h', 'i', 'j']

print(list_1)

# Locate the missing elements in list_1 and their left neighbors
missing_elem_and_neighbor = []
for ind, elem in enumerate(list_2):
    if elem not in list_1:
        if ind > 0:
            missing_elem_and_neighbor.append((elem, list_2[ind-1]))
        else:
            missing_elem_and_neighbor.append((elem, None))

# Insert missing elements into list_1
for elem, nei in missing_elem_and_neighbor:
    if nei:
        ind_nei = list_1.index(nei)
        list_1.insert(ind_nei+1, elem)
    else:
        if list_1[0] in list_2:
            # Goes before 0 in list_1
            list_1.insert(0, elem)
        else:
            # Assumption - right after the first in list_1
            list_1.insert(1, elem)

print(list_1)
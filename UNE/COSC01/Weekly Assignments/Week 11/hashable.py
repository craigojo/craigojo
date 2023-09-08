def find_map(maps, k): 
    index = hash(k) % len(maps)
    return maps[index]
# n is a count of the items
# in the hashtable
def add(maps, n, k, v):
    if n == len(maps):
        maps = resize(maps, n)
    map = find_map(maps, k)
    map.append((k, v))
    return maps
def get(maps, target):
    map = find_map(maps, target)
    for key, val in map:
        if key == target:
            return val
    raise KeyError

def resize(maps, n):
    new_maps = []
    for i in range(2 * n):
        new_maps.append([])
    c = 0
    for map in maps:
        for k, v in map:
            add(new_maps,c,k,v)
            c = c + 1
    return new_maps


maps = [[]]
maps = add(maps, 0, 1, 2)
maps = add(maps, 1, 2, 3)
get(maps, 1)
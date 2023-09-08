def find_map(maps, k):
    index = hash(k) % len(maps)
    return maps[index]

def add(maps, k, v):
    map = find_map(maps, k)
    map.append((k, v))
    return maps

def get(maps, target):
    map = find_map(maps, target)
    for key, val in map:
        if key == target:
            return val
    raise KeyError


maps = []
for i in range(100):
    maps.append([])
    maps = add(maps, 1, 2)
    get(maps, 1)
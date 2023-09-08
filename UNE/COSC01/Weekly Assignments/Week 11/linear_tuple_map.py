def add(map, k, v):
    map.append((k, v))
    return map

def get(map, target):
    for key, val in map:
        if key == target:
            return val
    raise KeyError


map = []
map = add(map, 1, 2)
get(map, 1)
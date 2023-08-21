
def has_duplicates(l):

    seen = []
    
    for i in l:
        if i in seen:
            print(seen)
            print(i)
            return True
        seen.append(i)
    print(seen)     
    return False

l = ["cat", "car","car", "cat", "dog"]
has_duplicates(l)




        
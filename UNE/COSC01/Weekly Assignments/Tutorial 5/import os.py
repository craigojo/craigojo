import os
def list_files(base, suffix):
    assert os.path.isdir(base)
    for file in os.listdir(base):
        path = os.path.join(base, file)
        if path.endswith(suffix):
            print(path)
    if os.path.isdir(path):
        list_files(path, suffix)





# The parameter base is a string of the directory you want to recursively explore, 
# so if you want to check a directory 'test' in home, you will pass '~/test' as base. 
# Suffix is the suffix of the file you are interested to find, e.g. '.txt' or '.py', ...

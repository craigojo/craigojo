import glob
import os



txtfiles = []
def files():

    cwd = os.getcwd()
    print(cwd)
    dir = os.listdir(cwd)
    print(dir)
    os.path.join(cwd, "report.txt")
    for file in glob.glob("*.md"):
        txtfiles.append(file)

files()
print(txtfiles)

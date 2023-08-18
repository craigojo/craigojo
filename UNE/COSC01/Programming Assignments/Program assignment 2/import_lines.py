line = "routes.txt"
lines = []



with open(line) as f:
    lines = [lin.rstrip() for lin in f]
print(lines)


#strip removes carriage return  \n fro imported file

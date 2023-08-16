"""
Bobby
Word Concordance (word frequency) 5_8
"""

# retrieve words from text file
f = "data.txt"
f = open(f,'r')

wli = [] # word list

# parse word file into individual words, sort,  and then populate into word list
for l in f:
    l = l.split()    # parse into individual words

    for w in l:
        wli.append(w) # populate word list with words

wli.sort() # word list sorts words by alpha order

wd = {}   # word dictionary for words with word counts

# count words in word list and then populate word dictionary
for w in wli:
    wd[w] = wli.count(w)

# retrieve words and word counts from word dictionary
print('\n{:^8}{:^8}'.format('Word','Count')) # format columns with headers
for w in wd:
    print('{:^8}{:^8d}'.format(w,wd[w]))     # format data and print

print("")
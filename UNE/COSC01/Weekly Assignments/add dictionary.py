# create a dictionary
d = {
    'value1': 5,
    'value2': 4,
    'value3': 3,
    'value4': 2,
    'value5': 10,
}
# create a variable to store result
answer = 1
val=list(d.values())
 
# run a loop
for i in val:
    answer = answer*i
# print answer
print(answer)
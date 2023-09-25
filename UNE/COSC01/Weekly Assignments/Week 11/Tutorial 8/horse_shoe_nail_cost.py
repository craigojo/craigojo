
# total_cost = -1
# cost_of_nail = 1
# for horse_foot in range(4):
#    for nail in range(6):
#       cost_of_nail = 2* cost_of_nail
# total_cost += cost_of_nail
# print("The total cost to shoe the horse would be ${0:.2f}".format(total_cost / 100))


total_cost = 0
cost_of_nail = 1
for horse_foot in range(4):
   for nail in range(6):
      total_cost += cost_of_nail
      cost_of_nail = 2*cost_of_nail

print("The total cost to shoe the horse would be ${0:.2f}".format(total_cost / 100))
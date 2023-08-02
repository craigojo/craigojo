'''Please enter the route number: 123
Please enter the number of stops on this route: 4
How many passengers were waiting for the bus at stop #1? 5
How many passengers left the bus at stop #2? 5
How many passengers were waiting for the bus at stop #2? 5
How many passengers left the bus at stop #3? 5
How many passengers were waiting for the bus at stop #3? 5
How many passengers left the bus at stop #4? 5
Route number: 123
Happy customers: 15
Unhappy customers: 0
Ratio of happy to unhappy customers: 0.00'''

max_passengers = 35
max_passengers = int(max_passengers)
unhappy = 0
unhappy = int(unhappy)
current_load = 0
current_load = int(current_load)
stop = -1


route_number = int(input("What is the route number: "))
start = int(input("How many passengers waiting for bus at start of route? :"))
if start > max_passengers:
    print("Sorry, our maximum capacity is 35, some will need to wait for next bus")
    unhappy += start - max_passengers

number_of_stops = int(input("Please enter the number of stops on this route: " ))




while stop < number_of_stops:
    
    get_on = int(input("How many waiting to get on at this stop?"))
    get_off = int(input("How many to depart at this stop?"))
    stop += 1
    vacated_capacity = current_load - get_off
    available_capcity = max_passengers - vacated_capacity
    new_load = available_capcity + get_on
    if new_load > max_passengers:
        over_load = new_load - max_passengers
        print (f"Not enough capacity for all passengers, {over_load} will need to wait for next bus")
        unhappy += over_load


    if get_on > 35:
        print ("Too many passengers, some will need to stay")
        unhappy += get_on - max_passengers
print(unhappy)
        


            
    
    






# n = int(input('How many stops does this route have?'))       #n is the number of items you want to enter
# dict ={}                     
# for i in range(n):        
#     text = input().split()     #split the input text based on space & store in the list 'text'
#     dict[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
# print(dict)




# x = how many stops will there be 
# stop = (x)
# dict{}
# while i < x:
     
#     dict['Stop' [stop] ]"hot many passengers at stop  :" [stop] )
#     stop += stop


# bus=Bus(int(input('Bus number:')))


# stops=int(input('Stops:'))
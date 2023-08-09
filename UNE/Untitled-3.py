

current_load = 10
stop = 1
get_off = int()

while True:
    get_off =  (f"How many to depart at bus stop {stop + 1}?")
    try:
        get_off = int(get_off)
        break
    except ValueError:
        print("Please enter a number")  
    try:
        get_off < current_load
        break
    except:
        get_off > current_load
        print("Departing passengers cannot be larger than current passengers in the bus")
get_off = int(get_off)
print(f"Passengers waiting to depart bus at stop {stop + 1} = {get_off}")
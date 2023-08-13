# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it
class Bus:
    def __init__(self, number):
        self.capacity = 35
        self.number = number
        self.happy=0
        self.inside=0
        self.total_passengers=0
        self.left_total=0

    def take_passengers(self,passengers_in,passengers_out = 0):
 
        self.total_passengers += passengers_in
 
        if self.inside == 0:
            if passengers_in < 35:
                self.inside+=passengers_in
            else:
                left_on_stop_sorry=(passengers_in - 35)
                self.inside+=passengers_in - left_on_stop_sorry
                bus.left_total += left_on_stop_sorry
        else:
            if passengers_in < (35 - self.inside + passengers_out):
                self.inside+=passengers_in - passengers_out
            else:
                left_on_stop_sorry=(passengers_in - (35 - self.inside + passengers_out))
                self.inside+=passengers_in - left_on_stop_sorry
                bus.left_total += left_on_stop_sorry
  


bus=Bus(int(input('Bus number:')))


stops=int(input('Stops:'))



for i in range(stops):
    on=int(input('Passengers on:'))
    if (bus.inside > 0):
        off = int(input('Passengers left:'))
        bus.take_passengers(on,off)
    else:
        bus.take_passengers(on)
    print('Cool! going to the next stop')




ratio = bus.total_passengers/(bus.total_passengers - bus.left_total)

print(f'Ratio:{ratio}')
print(f'Total happy:{bus.total_passengers - bus.left_total}')
print(f'Unhappy:{bus.left_total}')


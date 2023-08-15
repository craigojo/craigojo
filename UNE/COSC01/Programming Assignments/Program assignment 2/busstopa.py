def main():
    route_number = input("Enter bus route number: ")
    num_stops = int(input("Enter number of stops along the route: "))

    passengers_on_bus = 0
    for stop in range(1, num_stops + 1):
        print(f"\nStop {stop}")
        
        passengers_waiting = int(input("Enter number of passengers waiting at this stop: "))
        
        while True:
            passengers_exiting = int(input("Enter number of passengers exiting the bus at this stop: "))
            if passengers_exiting > passengers_on_bus:
                print("Passengers exiting cannot exceed passengers on the bus.")
            else:
                break
        
        passengers_on_bus = min(passengers_on_bus - passengers_exiting + passengers_waiting, 35)
        print(f"Passengers on the bus after stop {stop}: {passengers_on_bus}")

    print("\nEnd of bus route.")

if __name__ == "__main__":
    main()

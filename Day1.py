bikes = {"Pulsar": 20, "Unicorn": 30, "Royal Enfield": 10}


def display():
    for (bike, no) in zip(bikes.keys(), bikes.values()):
        print("Bike:", bike, "|", "Numbers available: ", no)


def book(bike_name, num):
    for values in bikes:
        bikes[values] = int(bikes[values])
    if bike_name in bikes.keys():
        value = bikes.get(bike_name)
        if (num <= value):
            value = value - num
            bikes.pop(bike_name)
            bikes[bike_name] = value
            print("You have successfully booked %d %s" % (num, bike_name))
        else:
            print("Required number of bikes not available")
    else:
        print("Required Bike not available")


def ret_bike(bike_name, num, hours):
    cost = num * hours * 50
    for values in bikes:
        bikes[values] = int(bikes[values])
        if bike_name in bikes.keys():
            value = bikes.get(bike_name)
            value = value + num
            bikes.pop(bike_name)
            bikes[bike_name] = value
    print("**********************************")
    print("You have returned  ", bike_name)
    print("Number of bikes returned ", num)
    print("Total amount payable is Rs :", cost)
    print("***********************************")


def main():
    print()
    print("************BIKE RENTAL SYSTEM***********")
    print(" ******50 rs per hour for rentals********")
    print("1. Display details of bikes")
    print("2. Rent bikes")
    print("3. Return bikes")
    print("*****************************************")
    choice = input("Enter choice: ")
    choice = int(choice)
    if choice == 1:
        display()
    if choice == 2:
        bike_name = input("Enter name of bike")
        no_bikes = input("Enter number of bikes")
        no_bikes = int(no_bikes)
        book(bike_name, no_bikes)
    if choice == 3:
        bike_name = input("Enter name of bike")
        if bike_name in bikes.keys():
            no_bikes = input("Enter number of bikes")
            no_bikes = int(no_bikes)
            hours = input("Number of hours")
            hours = int(hours)
            ret_bike(bike_name, no_bikes, hours)
        else:
            print("Check the bike name")

if __name__ == "__main__":
    main()

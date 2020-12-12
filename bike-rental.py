from datetime import datetime
bike_l = {"Pulsar": 20, "Unicorn": 30, "Royal Enfield": 10}


class Display:
    def __init__(self):
        self.bikes = {}

    def display(self, bikes):
        print("************ BIKES AVAILABLE ******************")
        for (bike, no) in zip(bikes.keys(), bikes.values()):
            print("Bike:", bike, "|", "Numbers available: ", no)
        print("***********************************************")


class Bike(Display):
    def __init__(self):
        self.bikes = {}
        self.bike_name = ""
        self.number = 0

    def rent(self, bikes, bike_name, number):
        self.bikes = bikes
        self.bike_name = bike_name
        self.number = number
        if self.bike_name in self.bikes.keys():
            value = self.bikes.get(bike_name)
            newval = value-self.number
            if(newval >= 0):
                self.bikes[self.bike_name] = newval
                print("You have rented: ", self.bike_name)
                print("Numbers Rented:", self.number)
                print("*****************************")
                print()
                Display.display(self, bike_l)
            else:
                print("Required Number of bikes not available")
        else:
            print("Type a valid bike name")

    def ret_bike(self, bikes, bike_name, number, hours_used):
        if bike_name in bikes.keys():
            cost = hours_used*number*50
            value = bikes.get(bike_name)
            newval = value+number
            bikes[bike_name] = newval
            print("*******************************")
            print("You have returned:", bike_name)
            print("Number Returned:", number)
            print("Amount Payable:", cost)


class Customer(Bike, Display):
    def __init__(self):
        self.user_n = ""
        self.phone_n = ""

    def c_rent(self, user_n, phone_n, bikes, bike_name, number):
        if bike_name in bikes.keys():
            print("***************************")
            print("UserName: ", user_n)
            print("Phone number: ", phone_n)
            Bike.rent(self, bikes, bike_name, number)
        else:
            print("\nPlease Enter a valid bike name")

    def c_return(self, bike, bike_name, number, hours_used):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        Bike.ret_bike(self, bike, bike_name, number, hours_used)
        print("You have returned the bike at ", current_time)
        print()
        print("Database Updated")
        print("New Count of Bikes")
        print()
        Display.display(self, bike)


def main():
    print("***********************************")
    print("Bikes at 50rs per hour")
    print("\n1. Display Bike Details")
    print("2. Rent Bike")
    print("3. Return Bike")
    print()
    print("**********************************")
    choice = input("Enter Choice: ")

    if choice == "1":
        dis = Display()
        dis.display(bike_l)
    if choice == "2":
        usrname = input("Enter User Name: ")
        phoneno = input("Enter Phone Number: ")
        bike_n = input("Enter Name of Bike to rent: ")
        number = int(input("Enter Number of bikes to rent: "))
        ren = Customer()
        ren.c_rent(usrname, phoneno, bike_l, bike_n, number)
    if choice == "3":
        bike_n = input("Enter Name of Bike to return: ")
        number = int(input("Enter Number of bikes to return"))
        hours_used = int(input("Enter Number of hours used"))
        retu = Customer()
        retu.c_return(bike_l, bike_n, number, hours_used)


if __name__ == "__main__":
    main()

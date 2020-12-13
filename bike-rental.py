import os
import re
from datetime import datetime
bike_l = {"Pulsar": 20, "Unicorn": 30, "Royal Enfield": 10}

'''Class to Display Details'''


class Display:
    def __init__(self):
        self.bikes = {}

    def display(self, bikes):
        self.bikes = bikes
        print("************ BIKES AVAILABLE ******************")
        for (bike, no) in zip(self.bikes.keys(), self.bikes.values()):
            print("Bike:", bike, "|", "Numbers available: ", no)
        print("***********************************************")

'''Class for renting and returning'''


class Bike(Display):
    def __init__(self):
        self.bikes = {}
        self.bike_name = ""
        self.number = 0
        self.hours_used = 0

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
                os.system('pause')
                Display.display(self, bike_l)
            else:
                print("Required Number of bikes not available")
        else:
            print("Type a valid bike name")

    def ret_bike(self, bikes, bike_name, number, hours_used):
        self.bikes = bikes
        self.bike_name = bike_name
        self.number = number
        self.hours_used = hours_used
        if self.bike_name in self.bikes.keys():
            cost = self.hours_used*self.number*50
            value = self.bikes.get(self.bike_name)
            newval = value+self.number
            bikes[bike_name] = newval
            print("*******************************")
            print("You have returned:", self.bike_name)
            print("Number Returned:", self.number)
            print("Amount Payable:", cost)

'''Customer Class'''


class Customer(Bike, Display):
    def __init__(self):
        self.user_n = ""
        self.phone_n = ""

    def c_rent(self, user_n, phone_n, bikes, bike_name, number):
        self.user_n = user_n
        self.phone_n = phone_n
        if bike_name in bikes.keys():
            print("*********** BILL **************")
            print("UserName: ", self.user_n)
            print("Phone number: ", self.phone_n)
            Bike.rent(self, bikes, bike_name, number)
        else:
            print("\nPlease Enter a valid bike name")

    def c_return(self, bike, bike_name, number, hours_used):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        Bike.ret_bike(self, bike, bike_name, number, hours_used)
        print("You have returned the bike at ", current_time)
        print()
        os.system('pause')
        print("Database Updated")
        print("New Count of Bikes")
        print()
        Display.display(self, bike)

'''Main Function'''


def main():
    print("*************** MAIN MENU *******************")
    print("        Bikes at 50rs per hour               ")
    print("\n1. Display Bike Details")
    print("2. Rent Bike")
    print("3. Return Bike")
    print("4. Exit")
    print()
    print("*********************************************")
    choice = input("Enter Choice: ")

    if choice == "1":
        dis = Display()
        dis.display(bike_l)
        os.system('pause')
        main()
    if choice == "2":
        usrname = input("Enter User Name: ")
        phoneno = input("Enter Phone Number: ")
        ''' Regex to Match Phone Number'''
        number = re.match("[0-9]{10}$", phoneno)
        if number is None:
            print("Invalid Phone Number! Try Again")
            os.system('pause')
            main()
        else:
            bike_n = input("Enter Name of Bike to rent: ")
            number = int(input("Enter Number of bikes to rent: "))
            ren = Customer()
            ren.c_rent(usrname, phoneno, bike_l, bike_n, number)
            os.system('pause')
            main()
    if choice == "3":
        bike_n = input("Enter Name of Bike to return: ")
        number = int(input("Enter Number of bikes to return: "))
        hours_used = int(input("Enter Number of hours used: "))
        retu = Customer()
        retu.c_return(bike_l, bike_n, number, hours_used)
        os.system('pause')
        main()
    if choice == "4":
        exit()


if __name__ == "__main__":
    main()

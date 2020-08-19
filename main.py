from computer import computer
from computer import laptop
from computer import desktop
import sys


laptop0 = laptop("L001", 16, 512, 3.2, 0.99)
laptop1 = obj = laptop("L002", 16, 1000, 3.2, 0.99)
desktop0 = obj = desktop("D001", 32, 1000, 4.2, "1080p")
desktop1 = obj = desktop("D002", 32, 2000, 4.0, "4k")

laptops = [laptop0, laptop1]
desktops = [desktop0, desktop1]
userInput = 0
while True:
    print("Hello! This is my IT sales system")
    print("1. View all sales")
    print("2. Add desktop sale")
    print("3. Add laptop sale")
    print("4. Exit")

    userInput = input('Enter the menu number desired')

    if userInput == '1':
        y = 0
        z = 0
        for x in laptops:

            print("ComputerID:")
            print(laptops[y].computerID)
            print("Memory:")
            print(laptops[y].memory)
            print("Storage:")
            print(laptops[y].storage)
            print("Clock Speed:")
            print(laptops[y].clockspeed)
            print("Weight")
            print(laptops[y].weight)
            print("")
            y = y+1
        for x in desktops:

            print("ComputerID:")
            print(desktops[z].computerID)
            print("Memory:")
            print(desktops[z].memory)
            print("Storage:")
            print(desktops[z].storage)
            print("Clock Speed:")
            print(desktops[z].clockspeed)
            print("Monitor")
            print(desktops[z].monitor)
            print("")
            z = z+1

    elif userInput == '2':
        while True:
            print("Please enter Computer ID")
            tempCID = input()
            tempCID.upper()
            if (tempCID.startswith('D')):
                break
            else:
                print("Desktop Computer ID must start with 'D'")

        print("Please enter Memory")
        tempMe = input()
        print("Please enter Storage")
        tempS = input()
        print("Please enter Clock Speed")
        tempCS = input()
        print("Please enter Monitor")
        tempMo = input()
        temp = obj = desktop(tempCID, tempMe, tempS, tempCS, tempMo)
        desktops.append(temp)
        print("Sale added")
    elif userInput == '3':
        while True:
            print("Please enter Computer ID")
            tempCID = input()
            tempCID.upper()
            if (tempCID.startswith('L')):
                break
            else:
                print("Laptop Computer ID must start with 'L'")
        print("Please enter Memory")
        tempMe = input()
        print("Please enter Storage")
        tempS = input()
        print("Please enter Clock Speed")
        tempCS = input()
        print("Please enter Weight")
        tempW = input()
        temp = obj = laptop(tempCID, tempMe, tempS, tempCS, tempW)
        desktops.append(temp)
        print("Sale added")

    if (userInput == '4'):
        break

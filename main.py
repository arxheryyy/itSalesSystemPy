from computer import computer
from computer import laptop
from computer import desktop
from tkinter import *
from tkinter.ttk import *

laptop0 = laptop("L001", 16, 512, 3.2, 0.99)
laptop1 = obj = laptop("L002", 16, 1000, 3.2, 0.99)
desktop0 = obj = desktop("D001", 32, 1000, 4.2, "1080p")
desktop1 = obj = desktop("D002", 32, 2000, 4.0, "4k")

laptops = [laptop0, laptop1]
desktops = [desktop0, desktop1]
top = Tk()
top.geometry("200x200")


def buttonTest():
    print("works")


def showsales():
    window = Toplevel(top)
    window.title("show sales")
    window.geometry("200x200")
    Label(window, text="show sales").pack()
    y = 0
    for x in laptops:
        Label(window, text="ComputerID").pack()
        Label(window, text=laptops[y].computerID).pack()
        Label(window, text="Memory").pack()
        Label(window, text=laptops[y].memory).pack()
        Label(window, text="Storage").pack()
        Label(window, text=laptops[y].storage).pack()
        Label(window, text="Clock Speed").pack()
        Label(window, text=laptops[y].clockspeed).pack()
        Label(window, text="Weight").pack()
        Label(window, text=laptops[y].weight).pack()
        Label(window, text="").pack(padx=10, pady=10)
        y = y+1

    z = 0
    for x in desktops:
        Label(window, text="ComputerID").pack()
        Label(window, text=desktops[z].computerID).pack()
        Label(window, text="Memory").pack()
        Label(window, text=desktops[z].memory).pack()
        Label(window, text="Storage").pack()
        Label(window, text=desktops[z].storage).pack()
        Label(window, text="Clock Speed").pack()
        Label(window, text=desktops[z].clockspeed).pack()
        Label(window, text="Monitor").pack()
        Label(window, text=desktops[z].monitor).pack()
        Label(window, text="").pack(padx=10, pady=10)
        z = z + 1


def addD():
    window = Toplevel(top)
    window.title("Add desktop sale")
    window.geometry("200x200")
    Label(window, text="Add desktop sale").pack()
    Label(window, text="ComputerID").pack()
    entry1 = Entry(window)
    entry1.pack()

    def storeCompID():
        userInput = entry1.get()
        return userInput
    Button(window, text="Okay", command=storeCompID).pack()

    Label(window, text="Memory").pack()
    entry2 = Entry(window)
    entry2.pack()

    def storeMem():
        userInput = entry2.get()
        return userInput
    Button(window, text="Okay", command=storeMem).pack()

    Label(window, text="Storage").pack()
    entry3 = Entry(window)
    entry3.pack()

    def storeSto():
        userInput = entry3.get()
        return userInput
    Button(window, text="Okay", command=storeSto).pack()

    Label(window, text="Clock Speed").pack()
    entry4 = Entry(window)
    entry4.pack()

    def storeCS():
        userInput = entry4.get()
        return userInput
    Button(window, text="Okay", command=storeCS).pack()

    Label(window, text="Monitor").pack()
    entry5 = Entry(window)
    entry5.pack()

    def storeMon():
        userInput = entry5.get()
        return userInput
    Button(window, text="Okay", command=storeMon).pack()

    def buildD():
        tempCID = storeCompID()
        tempMe = storeMem()
        tempS = storeSto()
        tempCS = storeCS()
        tempMo = storeMon()
        temp = obj = desktop(tempCID, tempMe, tempS, tempCS, tempMo)
        desktops.append(temp)
        Label(window, text="Sale Added").pack()

    Button(window, text="Add Desktop", command=buildD).pack()


def addL():
    window = Toplevel(top)
    window.title("Add Laptop sale")
    window.geometry("200x200")
    Label(window, text="Add Laptop sale").pack()
    Label(window, text="ComputerID").pack()
    entry1 = Entry(window)
    entry1.pack()

    def storeCompID():
        userInput = entry1.get()
        return userInput
    Button(window, text="Okay", command=storeCompID).pack()

    Label(window, text="Memory").pack()
    entry2 = Entry(window)
    entry2.pack()

    def storeMem():
        userInput = entry2.get()
        return userInput
    Button(window, text="Okay", command=storeMem).pack()

    Label(window, text="Storage").pack()
    entry3 = Entry(window)
    entry3.pack()

    def storeSto():
        userInput = entry3.get()
        return userInput
    Button(window, text="Okay", command=storeSto).pack()

    Label(window, text="Clock Speed").pack()
    entry4 = Entry(window)
    entry4.pack()

    def storeCS():
        userInput = entry4.get()
        return userInput
    Button(window, text="Okay", command=storeCS).pack()

    Label(window, text="Monitor").pack()
    entry5 = Entry(window)
    entry5.pack()

    def storeWe():
        userInput = entry5.get()
        return userInput
    Button(window, text="Okay", command=storeWe).pack()

    def buildD():
        tempCID = storeCompID()
        tempMe = storeMem()
        tempS = storeSto()
        tempCS = storeCS()
        tempW = storeWe()
        temp = obj = laptop(tempCID, tempMe, tempS, tempCS, tempW)
        laptops.append(temp)
        Label(window, text="Sale Added").pack()

    Button(window, text="Add Laptop", command=buildD).pack()


def quit():
    exit()


a = Button(top, text="View all sales", command=showsales)
a.pack(padx=10, pady=5)
b = Button(top, text="Add Desktop Sale", command=addD)
b.pack(padx=10, pady=5)
c = Button(top, text="Add Laptop Sale", command=buttonTest)
c.pack(padx=10, pady=5)
d = Button(top, text="Quit", command=quit)
d.pack(padx=10, pady=5)
top.mainloop()


def dIdCheck(computerID):
    bool = False
    y = 0
    x = 0
    z = 0
    if(computerID.startswith("L")) and len(computerID) == 4:
        z = 1

    for x in desktops:
        if (computerID == desktops[y].computerID):
            x = 0
        else:
            x = 1
        y = y + 1
    if(x == 1 and z == 1):
        bool = True
        return bool


def lIdCheck(computerID):
    bool = False
    y = 0
    x = 0
    z = 0
    if(computerID.startswith("L")) and len(computerID) == 4:
        z = 1

    for x in laptops:
        if (computerID == laptops[y].computerID):
            x = 0
        else:
            x = 1
    if(x == 1 and z == 1):
        bool = True
        return bool


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
            bool = dIdCheck(tempCID)
            if (bool):
                break
            else:
                print("Desktop Computer ID must start with 'D'")
                print("")
                print("Computer ID must have 3 digits behind it.")

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
            bool = lIdCheck(tempCID)
            if (bool):
                break

            else:
                print("Desktop Computer ID must start with 'L'")
                print("")
                print("Computer ID must have 3 digits behind it.")
        print("Please enter Memory")
        tempMe = input()
        print("Please enter Storage")
        tempS = input()
        print("Please enter Clock Speed")
        tempCS = input()
        print("Please enter Weight")
        tempW = input()
        temp = obj = laptop(tempCID, tempMe, tempS, tempCS, tempW)
        laptops.append(temp)
        print("Sale added")

    if (userInput == '4'):
        break

"""Coin estimator practice."""
cent = 0
nickel = 0
dime = 0
quarter = 0
halfDollar = 0
prezDollar = 0
naDollar = 0
total = 0
while True:
    print("Select your coin type:")
    coin = input("1 - Cent\n"
                 "2 - Nickel\n"
                 "3 - Dime\n"
                 "4 - Quarter\n"
                 "5 - Half Dollar\n"
                 "6 - Presidental Dollar\n"
                 "7 - Native American Dollar\n")
    if coin == str(1):
        cent = input("Enter the weight of Pennies:\n")
        total = float(cent) / 2.5000
        print("The total number of coins is " + str(total))
    elif coin == str(2):
        print("This is a Nickel")
    elif coin == str(3):
        print("This is a Dime")
    elif coin == str(4):
        print("This is a Quarter")
    elif coin == str(5):
        print("This is a Half Dollar")
    elif coin == str(6):
        print("This is a Presidental Dollar")
    elif coin == str(7):
        print("This is a Native American Dollar")
    else:
        break

"""Coin estimator practice."""
print("Select your coin type:")
coin = input("1 - Cent\n"
             "2 - Nickel\n"
             "3 - Dime\n"
             "4 - Quarter\n"
             "5 - Half Dollar\n"
             "6 - Presidental Dollar\n"
             "7 - Native American Dollar\n")
print("")
weight = input("Enter total weight of coins:\n")


def estimate(coin, weight):
    """Math on estimating coins."""
    if coin == str(1):
        total = float(weight) / 2.500
    elif coin == str(2):
        total = float(weight) / 5.000
    elif coin == str(3):
        total = float(weight) / 2.268
    elif coin == str(4):
        total = float(weight) / 5.670
    elif coin == str(5):
        total = float(weight) / 11.340
    elif coin == str(6):
        total = float(weight) / 8.1
    elif coin == str(7):
        total = float(weight) / 8.1
    else:
        exit
    return(int(total))


total = estimate(coin, weight)


def roll(coin, total):
    """Estimate number of rolls required."""
    if coin == str(1):
        roll = total / 50
    elif coin == str(2):
        roll = total / 40
    elif coin == str(3):
        roll = total / 50
    elif coin == str(4):
        roll = total / 40
    elif coin == str(5):
        roll = total / 20
    elif coin == str(6):
        roll = total / 25
    elif coin == str(7):
        roll = total / 20
    else:
        exit
    print(int(roll))


print()
print()
print("The total number of coins is:")
print(estimate(coin, weight))
print("The number of rolls required is:")
roll(coin, total)

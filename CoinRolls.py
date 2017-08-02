print("what coin do you have?")
type_of_coin = input("1.penny\n2.nickel\n3.dime\n4.quarter:  ")
print("how much do your coins weigh?")
coin_weight = input("")
def determin_coin(x, y):
    total = int(coin_weight)
    if x == str(1):
        total = float(y) / 2.5
    elif x == str(2):
        total = float(y) / 5
    elif x == str(3):
        total = float(y) / 2.2
    elif x == str(4):
        total = float(y) / 5.6
    else:
        exit
    return(int(total))
total = determin_coin(type_of_coin, coin_weight)
def number_of_rolls(x, y):
        if x == str(1):
            roll = y / 50
        elif x == str(2):
            roll = y / 40
        elif x == str(3):
            roll = y / 50
        elif x == str(4):
            roll = y / 40
        else:
            exit
        print(int(roll))
print("you have this many coins:")
print(determin_coin(type_of_coin, coin_weight))
print("you need this many rolls:")
print(number_of_rolls(type_of_coin, total))

"""99 Bottles of beer program."""
bottles = 5
while bottles != 0:
    print(str(bottles) + " bottles of beer on the wall. "
            + str(bottles) + " bottles of beer. "
            + "take one down, pass it around;")
    print()
    bottles -= 1

    if bottles == 1:
        print(str(bottles) + " bottle of beer on the wall. "
            + str(bottles) + " bottle of beer. "
            + "take one down, pass it around;")
        print()
        print("No more bottles of beer on the wall!")
        bottles -= 1

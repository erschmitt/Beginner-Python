start_bottles = 99
while start_bottles != 0:
    print(str(start_bottles) + " bottles of beer on the wall, "
          + str(start_bottles) + " bottles of beer! "
                         + "take one down, pass it around")
    start_bottles -= 1
    if start_bottles == 1:
        print(str(start_bottles) + " bottle of beer on the wall, "
          + str(start_bottles) + " bottle of beer! "
                         + "take it down, pass it around ")
        print("no more bottles of beer!")
        start_bottles -= 1

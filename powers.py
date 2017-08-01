powers = input("Enter number of powers to find:  ")
powa = input("what are you raising it to:  ")
powList = []

for load in range(int(powers)):
   powList.append(input("Enter a number:  "))

for number in powList:
    total = int(number) ** int(powa)
    print(total)

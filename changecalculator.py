cost = float(input("how much did the item cost? "))
money_given = float(input("how much money did you give? "))
cost = int(cost * 100)
money_given = int(money_given * 100)
quarter = 25
dime = 10
nickel = 5
penny = 1
print(cost)
print(money_given)
money_back = int(money_given) - int(cost)
print(money_back)
figurequarter = money_back % quarter
print(figurequarter)
figuredime = figurequarter % dime
print(figuredime)
figurenickel = figuredime % nickel
print(figurenickel)
figurepenny = figurenickel % penny
print(figurepenny)

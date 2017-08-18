print("Change Calclator")
quarter = 25
dime = 10
nickel = 5
penny = 1
moneygiven = input("Enter how much money given: ")
citem = input("How much did the item cost?: ")
moneygiven = int(float(moneygiven) * 100)
citem = int(float(citem) * 100)
moneyback = moneygiven - citem
qmb = moneyback // quarter
partialtotal = moneyback - qmb * quarter
dmb = partialtotal // dime
dpartialtotal = partialtotal - dmb * dime
nmb = dpartialtotal // nickel
npartialtotal = dpartialtotal - nmb * nickel
pmb = npartialtotal // penny
ppartialtotal = npartialtotal - pmb * penny

print("You need %s quarters, %s dimes, %s nickels, %s pennies." % (qmb, dmb, nmb, pmb))

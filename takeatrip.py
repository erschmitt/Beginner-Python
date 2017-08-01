people = input("how many people are eating pasta?")
def standofpasta(amount):
    if people == str(1):
        print("use 20 ")
    elif people == str(2):
        print("use 40")
    elif people == str(3):
        print("use 80")
    elif people == str(4):
        print("use 120")
    elif people == str(5):
        print("use 150")
    elif people <= str(6):
        print("use a lot")
print(standofpasta(people))

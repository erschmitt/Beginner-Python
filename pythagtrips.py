will_smart = input("do you think will is smart? 1 for yes. 2 for no   ")
def will_determin(inteligence):
    if will_smart == str(2):
        print("you are wrong")
    elif will_smart == str(1):
        print("you are correct")
    elif will_smart <= str(3):
        print("try again")
print(will_determin(will_smart))

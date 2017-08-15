tri_sides = 3
tri_side_list = []

while True:
    for x in range(int(tri_sides)):
        tri_side_list.append(input("enter your sides: "))
        tri_side_list.sort()
    def tri_math(tri_side_list):
        if int(tri_side_list[0]) ** 2 + int(tri_side_list[1]) ** 2 == int(tri_side_list[2]) ** 2:
            print("this is a right triangle")
        else:
            print("this is not a right triangle")
    print(tri_math(tri_side_list))
    do_over = 1
    print("play again?")
    do_over = input("1 yes, 2 no: ")
    if do_over == str(1):
        tri_side_list.pop
    if do_over == str(2):
        break

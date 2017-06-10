"""Pythagorean Triples Checker for Python Practice."""
TriangleList = []

# print(TriangleList)

while True:
    FirstNum = input("Please enter the first number: ")
    SecondNum = input("Please enter the second number: ")
    ThirdNum = input("Please enter the third number: ")
    TriangleList.append(FirstNum)
    TriangleList.append(SecondNum)
    TriangleList.append(ThirdNum)
    TriangleList.sort()

    def TriangleFinder(TriangleList):
        """Trying to find triangles."""
        if int(TriangleList[0]) ** 2 + int(TriangleList[1]) ** 2 == \
                int(TriangleList[2]) ** 2:
            return("This is a right triangle")
        else:
            return("This is not a right triangle")
    print(TriangleFinder(TriangleList))
    print()
    print("Go again?")
    again = input("1 yes, 2 no: ")
    if again == str(2):
        break
    else:
        TriangleList = []
        print()

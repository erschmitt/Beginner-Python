data = []
print("This program will make mean, median and mode very easy!")
print("\nFirst, we need to enter some numbers!")

num=input("Type your first number: ")
while num:
    data.append(float(num))
    print("\n",data)
    num = input("Add another number, or press enter to move on.")
total = sum(data)
length = len(data)
print("The Mean Is:  ",total/length)
data.sort()
print("Here's the list in numerical order:  ", data)
oddness = length%2
half= length//2
if oddness == 1:
    print("The median is:  ",data[half])
else:
    low = float(data[half-1])
    high = float(data[half])
    print("The median is half way between", low, "and", high)
    print("That makes it:",low+(high-low)/2)
hits = []
for item in data:
    tally = data.count(item)
    values = (tally, item)
    if values not in hits:
        hits.append(values)
hits.sort(reverse=True)
if hits[0][0]>hits[1][0]:
    print("\n\nThe mode is:", hits[0][1], "hit appeared", hits[0][0], "times.")
else:
    print("There is not a mode")

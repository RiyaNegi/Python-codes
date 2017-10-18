import sys
print("lets get shwiftyyyyy")

stars = 9
space = 0

while (stars > 0):
    sys.stdout.write(" "*space)
    sys.stdout.write("*"*stars)
    space +=1
    stars -=2
    print("\n")

stars = 3
space = 3

while (stars < 10 and stars > 0):
    sys.stdout.write(" "*space)
    sys.stdout.write("*"*stars)
    space -= 1
    stars += 2
    print("\n")

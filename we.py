import sys
print("heyyyyyyyyy")


stars = 9
space = 0

while (stars > 0):
    sys.stdout.write(" "*space)
    sys.stdout.write("*"*stars)
    space +=1
    stars -=2
    print("\n")

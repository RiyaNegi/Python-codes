import sys
print("show me whatchyaaa got")

stars = 1
while (stars < 6 and stars > 0):
    sys.stdout.write("*"*stars)
    stars +=1
    print("\n")
    if (stars ==5):
        sys.stdout.write("*"*4)

space = 5
stars = 4
while (stars):
        sys.stdout.write(" "*space)
        sys.stdout.write("*"*stars)
        space += 1
        stars -=1
        print("\n")

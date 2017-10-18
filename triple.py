import sys
print("wuba luba dub dub")

stars=1
space = 5
while(space > 0):
    sys.stdout.write("*"*stars)
    sys.stdout.write(" "*space)
    sys.stdout.write("*"*stars)
    print("")
    stars += 1
    space -= 2

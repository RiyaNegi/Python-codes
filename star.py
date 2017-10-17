import sys
print("heelllooooo")

star=5
space=0

while(star != 0):
    sys.stdout.write(" "*space)
    sys.stdout.write("*"*star)
    print("\n")
    space+=1
    star-=1

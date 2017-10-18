import sys
print("m the danger")

print("    *")
space = 3
a = 1

while space >=0:
    sys.stdout.write(" "*space)
    sys.stdout.write("*")
    sys.stdout.write(" "*a)
    sys.stdout.write("*")
    print("")
    space-=1
    a+=2

space = 1
a = 5

while space <4:
    sys.stdout.write(" "*space)
    sys.stdout.write("*")
    sys.stdout.write(" "*a)
    sys.stdout.write("*")
    print("")
    space +=1
    a-=2
print("    *")

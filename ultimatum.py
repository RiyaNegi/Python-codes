import sys
print("its gonna be a goooood one")

sys.stdout.write("         *        ")
print("          *")
space = 8
a = 1

while space >=0:
    sys.stdout.write(" "*space)
    sys.stdout.write("*")
    sys.stdout.write(" "*a)
    sys.stdout.write("*")
    sys.stdout.write("  "*space)
    sys.stdout.write("*")
    sys.stdout.write(" "*a)
    sys.stdout.write("*")

    print("")
    space-=1
    a+=2
print("* * * * * * * * * * * * * * * * * * * *")
print("\n")
print("\n")
print("\n")


for i in range (1,2):
    print("     *")*i
for a in range (3,0,-1):
    print("     *")*a

x=1
while (x < 3):
    sys.stdout.write("     *\n"*x)
    x +=1


print("     *")
space = 2
a = 1

while space >=0:
    sys.stdout.write(" "*space)
    sys.stdout.write(" *")
    sys.stdout.write(" "*a)
    sys.stdout.write("  *")
    print("")
    space-=1
    a+=2

print("* * * * * *")

square =1
while ( square < 6 and square > 0 ):
    print("*         *")
    square +=1

print("* * * * * *")

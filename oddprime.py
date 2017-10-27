print ("yoooooo")

a = []

for x in range(3, 100):
    end_tak_chala = True
    for i in range(3, x, 2):
        if x%i == 0:
            print x, i
            end_tak_chala = False
            break
    if end_tak_chala:
        a.append(x)

print(a)

print("hell giters")

prime = True
x = 20
for i in range (2, x):
    if x!=i and (x%i) == 0:
        prime = False
    break

print(prime)

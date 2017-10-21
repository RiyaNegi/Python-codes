a, b = 8, 6
lcm = 0
i = a
while(lcm == 0):
    i += 1
    if i%a == 0 and i%b == 0:
        lcm = i

print(lcm)

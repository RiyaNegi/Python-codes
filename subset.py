a = [1, 5, 2, 9] # TRUE
a = [1, 5, 2, 9, 10] # FALSE
b = [5, 3, 1, 2, 9, 8]


def first_subset(a,b):
    matches = 0
    for i in range(0,len(a)):
        for x in range(0,len(b)):
            if a[i] == b[x]:
                matches += 1
    # return (matches == len(a))
    if matches == len(a):
        return True
    else:
        return False

print(first_subset(a, b))

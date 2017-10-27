a = [2, 32, 1, 4, 5, 8]
while True:
    swapped=-1
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            x=a[i]
            a[i]=a[i+1]
            a[i+1]=x
            swapped=i
    if swapped == -1:
        break
print(a)

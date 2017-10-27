print("heeey")

a = [4, 34, 1, 56, 9]
curr_no=11110
final=11110
b=[]
for i in a:
    for x in range(0,len(a)):
        if i!=a[x] and abs(i - a[x]) < curr_no:
            curr_no=abs(i-a[x])
            if curr_no < final:
                b = []
                b.append(i)
                b.append(a[x])
                final = curr_no

print(b)

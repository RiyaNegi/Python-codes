print("hellooo")
a = [3, 7, 18, 9, 10, 9, 4, 3]
current_no = 0
new = [ ]
for i in range(0,len(a)-1) :
    current_no = a[i]
    print(current_no)
    if a[i] > a[i+1]:
        new.append(a[i])


print(new)

print("fibo fibo")
a=[1,1,2,4,3,2,1,7,8,5,8,9,0,53,4,8,2,3,4,5,7]
for i in range(2,len(a)):
    store=0
    store=a[i-1]+a[i-2]
    a[i]=store
print(a)
add=0
for i in range(0,len(a)-1):
    ratio = (a[i+1])/(a[i])
    add += ratio

average= add/len(a)
print('average : '+ str(average))

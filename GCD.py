a, b = 24,54

gcd = 1

for i in range(1, a):
    if a%i == 0 and b%i == 0:
        gcd = i

print gcd

# print("aww hell naaaww")
#
# a, b = 8, 12
# arr_a=[]
# arr_b=[]
# arr_c=[]
#
# for i in range (1,a):
#     if a%i == 0:
#         arr_a.append(i)
#
# for i in range (1,b):
#     if b%i == 0:
#         arr_b.append(i)
#
# print (arr_a)
# print (arr_b)
#
# for x in range(0,len(arr_a)):
#     for y in range(0,len(arr_b)):
#         if arr_a[x] == arr_b[y]:
#             arr_c.append(arr_a[x])
#
# print(arr_c)
# print("the GCD of a and b is " + str(arr_c[len(arr_c)-1]))

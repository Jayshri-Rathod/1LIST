# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43,] 
# i=0
# even=0
# odd=0
# while i<len(elements):
#     if elements[i]%2==0:
#         even=even+1
#     else:
#         odd=odd+1
#     i+=1
# print(even,"even numbers",odd,"odd numbers")




elements=[1,2,3,4,5,6,7,8,9,10]
i=0
sumE=0
sumO=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even+=1
        sumE+=elements[i]
        print(elements[i],"even number")
    else:
        odd+=1
        sumO+=elements[i]
        print(elements[i],"odd number")
    i+=1
print(sumE)
print(sumO)

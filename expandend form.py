a=int(input("enter number"))
b=str(a)
l=len(b)
t=l-1
i=0
while i<len(b):
    code=int(b[i])
    num=(code)*10**t
    if i==0:
        print("'",num,end=" ")
    else:
        print(num,end=" ")
    if i!= len(b)-1:
        print("+",end=" ")
    i+=1
    t=t-1
print("'")
    
# a=int(input("enter number"))
# b=str(a)
# i=0
# while i<len(b):
#     print(int(b[i])**2,end=" ")
#     i+=1
main=["A","B"]
user=int(input("enter input number"))
i=0
a=[]
while i<len(main):
    j=1
    while j<=user:
        b=main[i]+str(j)
        a.append(b)
        j+=1
    i+=1
print(a)


# n=int(input("enter number"))
# i=0
# a=[]
# x=[]
# c="2"
# while i<=n:
#     b=c+"^"+str(i)
#     a.append(b)
#     y=int(c)**i
#     x.append(y)
#     i+=1
# print(x)
# print(a) 
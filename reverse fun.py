c=[]
a=int(input("please enter the total number of list elements"))
k=1
while k<=a:
    value=int(input("plz enter the value of elements"))
    c.append(value)
    k+=1
print(c)
i=0
while i<len(c):
    j=i+1
    while j<len(c):
        if c[i]>c[j]:
            d=c[i]
            c[i]=c[j]
            c[j]=d
        j+=1
    i+=1
print(c)
b=[]
i=1
while i<=len(c):
    b.append(c[-i])
    i+=1
print(b)
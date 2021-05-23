a=[4,7,2,9,10]
# a=[-2,-3,4,0,12]
# a=["d","y","w","y"]
b=[]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]>a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j+=1
    i+=1
print(a)
b=[]
i=1
while i<=len(a):
    b.append(a[-i])
    i+=1
print(b) 
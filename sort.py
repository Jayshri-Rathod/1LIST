b=[]
a=[4,7,6,3,2]
i=0
while i<len(a)+1:
    j=i+1
    while j<len(a)+1:
        if b[i]>b[j]:
            c=b[i]
            b[i]=b[j]
            b[j]=c
        j+=1
    i+=1
print(b)


a=[4,3,5,1,7,6,9,8,10]
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
num=int(input("enter number 1 to 10:-"))
if num%2==0:
    print("true")
else:
    print("false")

a=[1,2,3,[4,5,7],8,1,[1,1]]
i=0
sum=0
while i<len(a):
    if type(a[i])==type(a):
        j=0
        while j<len(a[i]):
            sum+=a[i][j]
            j+=1
    else:
        sum+=a[i]
    i+=1
print(sum)


Binary_numbers= [1, 0, 0, 1, 1,0,1, 1,0] 
c=[]
sum=0
decimal=0
i=0
lenth=len(Binary_numbers)
while i<lenth:
        a=lenth-i-1
        b=Binary_numbers[a]
        c.append(b)
        decimal=c[i]*2**i
        sum=sum+decimal
        i+=1
print(sum)

name=[ 1,2,3,4,2,1] 
c=[]
# i=0
# lenth=len(name)
# while i<lenth:
#     a=lenth-i-1
#     b=name[a]
#     c.append(b)
#     i+=1
# if c==name:
#     print("palidrome number hai") 
# else:
#     print("palindrom number nahi hai")
i=1
while i<=len(name):
    c.append(name[-i])
    i+=1
print(c)
if c==name:
    print("palindrome number")
else:
    print("not palindrome number")

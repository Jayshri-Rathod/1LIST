elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count=0
even=0
odd=0
sum=0
even_sum=0
odd_sum=0
i=0
while i<len(elements):
    count+=1
    sum+=elements[i]
    average=sum/len(elements)
    if elements[i]%2==0:
        even=even+1
        even_sum+=elements[i]
        average1=even_sum/len(elements)
    else:
        odd=odd+1
        odd_sum+=elements[i]
        average_O=odd_sum/len(elements)
    i+=1
print(count,":-","total elements",sum,"sum of elements",":-",average,"average of elements",":-" )
print(even,":-","even number",even_sum,":-","sum of even elements",average1,":-","average of even elements")
print(odd,":-","odd numbers",odd_sum,":-","sum of odd elements",average,":-","average of odd elements")

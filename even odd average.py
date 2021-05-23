elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
while i<len(elements):
    if elements[i]%2==0:
        even_sum+=elements[i]
        average_E=even_sum/len(elements)
    else:
        odd_sum+=elements[i]
        average_O=odd_sum/len(elements)
    i+=1
print(average_E,"average of even numbers")
print(average_O,"average of odd numbers")

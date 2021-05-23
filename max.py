numbers = [50, 40, 23, 70, 56, 12, 5, 10,] 
max=numbers[0]
i=0
while i<len(numbers):
    num=numbers[i]
    if num>max:
        max=num
    i+=1
print(max)

# for i in numbers:
#     if i>max:
#         max=i
# print(max)

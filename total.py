# marks = [[78, 76, 94, 86, 88],
# [91, 71, 98, 65, 76],
# [95, 45, 78, 52, 49]
# ] 
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 
i=0
total=0
while i<len(marks):
    j=0
    sum=0
    while j<len(marks[i]):
        num=(marks[i][j])
        sum=sum+num
        j+=1
    total+=sum
    i+=1
print(total)

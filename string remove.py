mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
x=mainStr.split()
i=0
subStr="over"
while i<len(x):
    if x[i]==subStr:
        i+=1
        continue
    # print(x[i],end=" ")
    i+=1
print(mainStr.replace("over","on"))














# n=[4,2,3,5,8,12,15]
# i=0
# a=0
# n=[]
# while i<15:
#     a+=1
#     if a not in n:
#         n.append(a)
#     i+=1
# print(n)





char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
a=[]
while i<len(char_list):
    j=0
    count=0
    b=[]
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count+=1
        j+=1
    b.append(char_list[i])
    b.append(count)
    if b not in a:
        a.append(b)
    i+=1 
print(a)












        


# list1=["hello","take"]
# list2=["dear","sir"]
# i=0
# y=[]
# while i<len(list1):
#     j=0
#     while j<len(list2):
#         b=(list1[i]+list2[j])
#         y.append(b)
#         j+=1
#     i+=1
# print(y)

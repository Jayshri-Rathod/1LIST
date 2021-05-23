kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
count1=0
count2=0
count3=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        count1+=1
    elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<=9999999:
        count2+=1
    else:
        count3+=1
    i+=1
print(count1,"carorpati hai")       
print(count2,"lakhpati hai")
print(count3,"Dilwale hai")
















# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# a=[]
# i=0
# while i<len(n):
#     j=1
#     while j<len(n):
#         if n[i]==n[j]:
#            a.append(i)
#         j+=1
#     i+=1
# print(a)

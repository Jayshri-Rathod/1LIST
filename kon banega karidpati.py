question_list = ["1.How many continents are there?",
    "2.What is the capital of India?",
    "3.NG mei kaun se course padhaya jaata hai?"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],
    ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
    ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = [3, 4, 1]
answer_list=[["(1)Four","(3)Seven",],
    ["(2)Bhopal","(4)Delhi"],
    ["(1)software engineering","(3)Tourism"]]
print("-:WELCOME TO KBC GAME:-")
print()
i=0
sum=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    a=i
    while j<len(options_list[i]):
        print(options_list[a][j])
        j+=1
    if count<1:
        num=input("do you want 5050 lifeline?")
        if num=="yes":
            print(answer_list[a])
            ans=int(input("enter your option number"))
            if ans==solution_list[i]:
                sum+=10000
                print("Congratualation, your answer is correct")
                print("you won Rs/",sum)
            else:
                print("your answer is wrong")
                print("Sorry, you can't play now")
                print("you won Rs/",sum)
                break
            count+=1
        else:
            print("you have alredy used")
            ans=int(input("enter your option number"))
            if ans==solution_list[i]:
                sum+=10000
                print("Congratualation, your answer is correct ")
                print("you won Rs/",sum)
            else:
                print("your answer is wrong")
                print("Sorry, you can't play now")
                print("you won Rs/",sum)
                break
    else:
        pass
        ans2=int(input("enter your answer number"))
        if ans2==solution_list[i]:
            sum+=10000
            print("Congratualation, your answer is correct ")
            print("you won Rs/",sum)
        else:
            print("your answer is wrong")
            print("Sorry, you can't play now")
            print("you won Rs/",sum)
            break
    i+=1
print("Thank you for playing game with me.")

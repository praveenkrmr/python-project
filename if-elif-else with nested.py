

x= input("enter the name of student:- ")
a=int(input("enter the mark of english:- "))
b=int(input("enter the mark of hindi:- "))
c=int(input("enter the mark of math:- "))
d=int(input("enter the mark of science:- "))
e=int(input("enter the mark of social science:- "))
print()

total_mark = a+b+c+d+e
print(x,"'s total mark is :- ",total_mark)

percent = total_mark/5
print(x,"got",percent,"%" ) 



#conditional-statement
if percent >= 90: # if-statement
    if percent >=95:     # if-statement nested
        print(x,"having grade A+")
    else:      # else-statement nested
        print(x,"having grade A")
elif percent >= 75:   # elif-statement
    print(x,"having grade B")
elif percent >= 60:    # elif-statement
    print(x,"having grade C")
else:   # else-statement
    print("fail")

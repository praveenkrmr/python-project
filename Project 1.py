'''
Student Result and Grade calculator 
by using Concepts :- condtional statement, loops

by Praveen Kumar Mishra


'''

while True:
    total_mark= 0
    
        
    print("\nEnter marks of 5 subjects")
    for i in range(1, 6):
        marks = int(input(f"Subject {i}: "))
        total_mark += marks
    percentage = total_mark / 5
    #print("Percentage =", percentage)
    if percentage > 100:
        print("Percentage =", percentage, "! someting is wrong !")
        print("Your input is wrong , please enter valid marks")
    elif percentage >= 90:
        print("Percentage =", percentage)
        print("Grade: A+")
    elif percentage >= 75:
        print("Percentage =", percentage)
        print("Grade: A")
    elif percentage >= 60:
        print("Percentage =", percentage)
        print("Grade: B")
    elif percentage >= 40:
        print("Percentage =", percentage)
        print("Grade: C")
    else:
        print("Percentage =", percentage)
        print("Fail")

        

    to_end = input("If u want to Check another student please type 'yes' to Exit press any key : ")
    if to_end.lower() != "yes":
        print("Program Ended")
        break

    

print ('''Praveen Kumar Mishra "Thank's you" for chossing this. ''')

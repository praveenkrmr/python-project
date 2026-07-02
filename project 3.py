'''
Quiz
by using Concepts :- condtional statement, loops ,list

by Praveen Kumar Mishra



'''

questions = [
    
("Is 0 an even number? ","yes"),
("Is 17 a prime number? ","yes"),
(" What is the square root of 81? ","9"),
(" Is π (Pi) a rational number? ","no"),
(" What is 7 × 8? ","56"),
(" Is every square a rectangle? ","no"),
("What is the value of 2⁵?  ","32"),
(" Is 1 a prime number? ","no"),
(" What is the cube of 4? ","64"),
(" Is 180° the sum of angles in a triangle? ","yes"),

]

while True:

    score = 0

    for question, answer in questions:

        user = input(question +" ")

        if user.lower() == answer:
            print("Correct")
            score += 1
        else:
            print("Wrong")

    print("\nYour Score =", score)

    if score == len(questions):
        print("Excellent!")

    elif score >= 7:
        print("Good")

    elif score >= 5:
        print("Good, need to improve")

    else:
        print("very poor , Need Practice")

    again = input('''enter "yes" to PLAY AGAIN or press any key to EXIT: ''')

    if again.lower() != "yes":
        print("Game Over")
        break


print ('''Praveen Kumar Mishra "Thanking you" for choosing this. ''')
print()
'''
ATM Machine 

by using Concepts :- condtional statement, loops

by Praveen Kumar Mishra


'''
balance = 10000

while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter ur Choice: "))
    print()

    if choice == 1:
        print("Ur Balance is  =", balance, )
        break

    elif choice == 2:
        amount = int(input("Deposit Amount: "))
        print()

        for i in range(1):
            balance += amount

        print(amount,"rs Credited in ur account \nnow your current Balance is ",balance)
        break

    elif choice == 3:
        amount = int(input("Withdraw Amount: "))
        print()

        if amount <= balance:
            balance -= amount
            print( "Please Collect Cash \nnow your current Balance is ",balance)
            
            break
        else:
            print("Insufficient Balance")     
            break

    elif choice == 4:
        print("Thank You")
        break

    elif choice > 4:
        print("Invalid Choice \nLogout!")
        break

    

print ('''Praveen Kumar Mishra "Thanking you" for choosing this. ''')
print()

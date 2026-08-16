'''1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions


'''

while True:
    print("Press 1 For to Check Prime NUmber ")
    print("Press 2 for to Check Palindrome Number ")
    print("Press 3 for to Print Reverse Number ")
    print("Press 4 for to Count Digits")
    print("Press 5 for EXIT.........")

    choice=int(input("Enter Your Choice "))

    match choice:
        case 1:
            num=int(input("Enter a Number "))
            temp=num
            if num<1:
                print("Not Prime Number ",temp)
            else:
                i=2
                while i<=num//2:
                    if temp%i==0:
                        print("Not Prime Number ",temp)
                        break
                else:
                    print("Prime Number : ",temp)
        
        case 2:
            num=int(input("Enter a Number "))
            rev=0
            temp=num
            
            while num>0:
                rev=rev*10+num%10
                num=num//10
            if rev==temp:
                print("Palindrome Number ",temp)

            else:
                print("Not Palindrome Number ",temp)

        case 3:
            num=int(input("Enter a Number :"))
            rev=0
            temp=num
            
            while num>0:
                rev=rev*10+num%10
                num=num//10
            print("Reverse of ",temp," is ",rev)

        case 4:
            num=int(input("Enter a Number "))
            Count=0
            temp=num
            
            while num>0:
               digit= num%10
               count=count+1

               num=num//10
            print("Digits :",count)

        case 5:
            print("EXIT..........................")

        case __:
            print("Invalid Choice Enter Again ")
            
    print("DO you want to Perform Again ........... ")
    again=input("yes/no ").lower()
    if again=="yes":
        continue
    else:
        print("Thank you .........")
        break
print("Thank You ")
    





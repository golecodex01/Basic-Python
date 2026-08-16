'''2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!

'''
salary=0
hra=0
da=0
tax=0
netsalary=0
while True :
    print("Press 1 . Enter Basic Salary ")
    print("Press 2 .  Calculate HRA (20%) and DA (10%) ")
    print("Press 3 . Calculate Net Salary ")
    print("Press 4 .  Tax Deduction ")
    print("Press 5 . Display Salary Slip ")
    print("Press 6 . Exit......")

    choice=int (input("Enter Your Choice : "))
    

    match choice :
        case 1:
            salary=int(input("Enter Your Salary : "))

            print("Your Salary Inserted SuccessFully ")

        case 2:
            if salary==0:
                print("Please Enter Salary First ")
            else :
                hra=salary*20/100
                da=salary*10/100
                print("HRA : ",hra )
                print("DA : ",da)

        case 3:
             if salary==0:
                print("Please Enter Basic Salary first") 
             else: 
                netsalary=salary+da+hra
                print("Net Salary (Before tax ) : ",netsalary)
        
        case 4: 
            if salary==0:
                print("Please Enter Basic Salary first") 
            else:   
                if salary>50000:
                    tax=salary/10
                    print("Salary After tax deduction : ",tax)
                else:
                     tax=salary/20
                     print("Salary After tax deduction : ",tax)

        case 5:
                if salary==0:
                    print("Please Enter Salary First ")
                else :
                
                    print("----- Salary Slip -----")
                    print("Basic Salary: ", salary)
 
                    print("HRA: " ,hra)
                    print("DA: ",da)
                    print("Net Salary: ",netsalary)
                    print("Tax: ",tax)
                    print("Final Salary: ",salary+hra+da-tax)
        
        case 6:
            print("EXIT...........")
            break

        case __:
            print("Please Enter a Valid Number From Menu  ")

    print("Do you Want to DO again ")
    print("YES/NO ")
    again=input().lower()

    if again=="yes":
        continue
    else :
        print("EXIT ....... ")
        break

print("Thank You ")







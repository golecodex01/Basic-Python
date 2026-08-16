'''
3.

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---

'''



balance=-1
interest=0

while True :
    print("Press 1. Deposit Money ")
    print("Press 2. Withdraw Money ")
    print("Press 3. Check Balance ")
    print("Press 4. Apply Interest ")

    choice=int(input("Enter Your Choice : "))

    match choice:
        case 1:
             balance=int(input("Enter Amount to Deposit "))
             print("Money Deposited SuccessFully ")

        case 2:
             if balance==-1:
                print("No balance available. Please deposit first")
             else:
                withdraw=int(input("Enter amount to withdraw "))
                if withdraw>=balance:
                    balance=balance-withdraw
                    print("Withdrawal SuccessFully ")
                else:
                    print("Insuffient Balance ")

        case 3:
              if balance==-1:
                print("No balance available. Please deposit first")
              else:
                print("Your Balance : ",balance)

        case 4 :
              if balance==-1:
                print("No balance available. Please deposit first")
              elif balance>50000:
                   interest=balance/10
                   balance=balance+interest
                   print("Intrest Added : ",interest)
                   print("Balance Updated : ",balance)
              else:
                   interest=balance/20
                   balance=balance+interest
                   print("Intrest Added : ",interest)
                   print("Balance Updated : ",balance)

        case 5:
               print("Exit........")
               break
        case __:
               print("Please Insert A Valid Choice ")

    print("Do Again(YES/No)")
    again=input().lower()
    if "yes" in again :
        continue
    else:
        print("Exit......")
        break

print("Thank you For Using ***GOLE BANK ATM*** ")
 

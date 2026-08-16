'''
Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit
'''
while True :
    print("PRESS 1. Enter Units Consumed ")
    print("PRESS 2. Calculate Bill Amount ")
    print("PRESS 3. Apply Surcharge ")
    print("PRESS 4. Display Final Bill ")
    print("PRESS 5. EXIT.......")

    option=int(input("Enter Your Choice "))

    match option:
        case 1:
            unit=int(input("Enter Units Consumed "))
            print("Units Entered SuccessFUlly ")
            
        case 2:
             if unit<=100:
                bill=unit*5
                print("Bill Amount :",bill)
                print("Explanation: ",unit,"* 5 =",unit*5)
             elif unit<=200:
                bill=100*5+(unit-100)*7
                print("Bill Amount :",bill)
                print("Explanation: "100*5 "=",100*5,",",unit-100,"* 7 = ",unit-100*7,",→ Total = ",bill)
             else:
                bill=unit*10
             print("Bill Amount : ",bill)
             print("Explanation: "100*5 "=",100*5,", 100 * 7 = ",100*7,","unit-200,"* 10 = ",unit-200*10,"→ Total = ",bill)  
        case 3:
              
              if bill>2000 :
               subcharge=bill/10
              else:
               subcharge=bill/20
             print("Subcharge  ",subcharge)
            
        case 4:
              print("Final Bill ",bill+subcharge)

        case 5:
              print("Exit...........")


'''
Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!'''


'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number

'''
number=input("ENter Your Number Plate : ")
fir=number[0].upper()
sec=number[1].upper()

if len(number)==10:
    if fir>='A' and fir<='Z' and sec>='A' and sec<='Z':
        third=number[2].upper()
        four=number[3].upper()
        if third >='0' and third<='9' and four >='0' and four<='9':

            print("Valid  Number Plate : ",number)



        else:
            print("Please ENter third and Fourth Character Must be Digit ")


    else:
        print("First and Second Character must be Alphabets ")


else:
    print("Number Plate Length Must be 10 ")
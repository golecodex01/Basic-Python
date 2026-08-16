'''6.
Railway Ticket PNR Analyzer
A railway department wants to verify whether a PNR number is valid.
Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits
Input:
Enter PNR: PNR123456789
Output:
Valid PNR Number
'''
pnr=input("Enter PNR : ").upper()

if len(pnr)==12:
    if pnr[0]=='P' and pnr[1]=='N' and pnr[2]=='R':
        for ch in range (3,len(pnr)-1):
            if pnr[ch].isdigit():
                

    else:
        print("PNR must be start with "PNR" ")


else:
    print("Lenght Should Be 12 ")

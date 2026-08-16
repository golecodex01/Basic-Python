bill= 2500
gst= 5
service = 10
frnd= 4

finalbill = bill + (bill *gst/100) + (bill*service/100)
each = finalbill / frnd

print("Final Bill =", finalbill)
print("Each Person Pays =", each)
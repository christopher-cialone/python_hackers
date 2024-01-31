bill_total = 210

discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    print("The bill was over 100 dollars")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("Bill is greater than 200")
    bill_total = bill_total - discount2
else:
    print("The bill was less than 100 dollars, you are the best")

print("Total Bill: "+ str(bill_total))



bill_total = 95

discount1 = 10

if bill_total > 100:
    print("The bill was over 100 dollars")
    bill_total = bill_total - discount1
else:
    print("The bill was less than 100 dollars, you are the best")

print("Total Bill: "+ str(bill_total))


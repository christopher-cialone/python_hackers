# functions - a set of instructions that take an input and return an output

# Defining Functions

# bill = 175.00

# tax_rate = 15

# total_tax = (bill * tax_rate) / 100.00

# print('Total tax', total_tax)

def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)
print('Total tax', calculate_tax(175.00, 15))

print('Total tax', calculate_tax(164.33, 22))
# call function to have this run

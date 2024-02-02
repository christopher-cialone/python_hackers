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

        # LEGB
        # Built-in Scope
        # Global Scope
        # Enclosing Scope
        # Local Scope

            # What is global scope?
my_global = 10
def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print('Access to GLobal', my_global)
        print('Access to enclosed', enclosed_v)
    fn2()

fn1()
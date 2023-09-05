income = 45000
print("Given income", income)
tax_payable = 0
taxable_income = 0
if (taxable_income < income):
    tax_payable = 0
    taxable_income += 10000

if (taxable_income < income):
    tax_payable += 10000 * 10/100
    taxable_income += 10000
    
if (taxable_income < income):
    tax_payable += (income - taxable_income) * 20/100
    taxable_income += income - taxable_income

print("Total tax to pay is", tax_payable)
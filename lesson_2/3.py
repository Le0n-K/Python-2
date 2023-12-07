a = int(input('Enter your sum: '))
b = int(input('Enter your % of tax: '))
tax = (a / 100) * b
print(f'This is your sum of tax - {tax:.2f}')
clean_income = a - tax
print(f'This is your clean income - {clean_income:.2f}')

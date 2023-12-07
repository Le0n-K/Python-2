a = int(input('What is the fuel consumption? '))
b = int(input('Todays price of 1 liter of fuel? '))
c = int(input('How many kilometers must be covered? '))
fuel = (a / 100) * c
print(f'The car will spend {fuel:.2f} liters of fuel per distance {c}')
price = fuel * b
print(f'Your price {price:.2f} of fuel!')

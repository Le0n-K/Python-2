import math

a = 2
b = 2.5
print(a, b)
print(type(a), type(b))

a = 6 + 4
print(a)
a = 20 - 3
print(a)
a = 4 * 7
print(a)
a = 45 / 5
print(a, type(a))
a = int(45 / 5)
print(a, type(a))
a = 10 / 3
print(a)
a = 10 / 3
print(round(a))
a = 10 / 3
print(round(a, 2))
a = 10 / 3
print(int(a))
print(int(1.75))
print(round(1.75))
print(round(1.75, 2))

print(math.ceil(8.3))
print(math.floor(8.3))

print(float(int(1.75)))           # преобразує, але не повертає десятичну частину


b = 5 ** 2
print(b)
b = pow(3, 4)    # теж саме що й **
print(b)
b = pow(25, 1/2)
print(b)
b = pow(25, 0.5)
print(b)
print(math.sqrt(36))


# є приорітет операцій
b = 25 ** 1 / 2
print(b)
b = 25 ** (1 / 2)
print(b)

x = 25 * 3 - 2 / 4 - 2
print(x)


unlucky_ticket = 458230

left_side = unlucky_ticket // 1000
print(left_side)
right_side = unlucky_ticket % 1000
print(right_side)

print(f'Calculating if ticket {unlucky_ticket} is lucky!')
# 458 = 4 + 5 + 8
x = left_side % 10
y = left_side // 10 % 10
z = left_side // 100
print(x, y, z)
print(f' Ticket left side {left_side} sum equals to {x + y + z}')

# 230 = 2 + 3 + 0
x = right_side % 10
y = right_side // 10 % 10
z = right_side // 100
print(x, y, z)
print(f' Ticket right side {right_side} sum equals to {x + y + z}')
print('Ticket is unlucky!')




lucky_ticket = 322151

left_side = lucky_ticket // 1000
print(left_side)
right_side = lucky_ticket % 1000
print(right_side)

print(f'Calculating if ticket {lucky_ticket} is lucky!')
# 322 = 3 + 2 + 2
x = left_side % 10
y = left_side // 10 % 10
z = left_side // 100
print(x, y, z)
print(f'Ticket left side {left_side} sum equals to {x + y + z}')

# 151 = 1 + 5 + 1
x = right_side % 10
y = right_side // 10 % 10
z = right_side // 100
print(x, y, z)
print('Ticket right side ' + str(right_side) + f' sum equals to {x + y + z}')
print('Ticket is lucky!')

x = 100 / 6
print(f'{x:.2f}')

print(divmod(10, 3))

print(type(z))
print(f'Is Z integer? {isinstance(z, int)}')
print(f'Is Z float?', isinstance(z, float))

# left_side, right_side = divmod(lucky_ticket, 1000)
# print(left_side)
# print(right_side)


x = input('Number >')
print(x, type(x))
x = float(x)
print(x, type(x))

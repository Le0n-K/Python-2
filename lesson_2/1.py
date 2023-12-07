import math

print('Do you want convert from degrees to radians?')
x = int(input(f'Enter the degrees: '))
y = math.radians(x)
print(f'This is convert radians - {y:.5f}')


print('Do you want convert from radians to degrees ?')
a = int(input(f'Enter the radians: '))
b = a * 180 / math.pi
print(f'This is convert degrees - {b:.5f}')

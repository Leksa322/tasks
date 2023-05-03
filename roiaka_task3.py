# Introduction to programming, Lab № 3
# Roiaka Oleksii IKM-221a

import math as m

print('Introduction to programming, Lab № 3')
print('Roiaka Oleksii IKM-221a')

TEMPLATE = "Enter {}"
x = int(input(TEMPLATE.format('x: ')))
a = int(input("Enter a: "))

if (25-x*x) < 0 or x-3 == 0:
    raise Exception("A function under the square root can not be negative or Can not devide by zero")
else:
    result = (m.sqrt(25-x*x)+2*a/(x-3))
    print(f"Result: {result}")

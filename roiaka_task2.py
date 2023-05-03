print("Introduction to programming, Lab № 2")
print("Roiaka Oleksii IKM-221a")

TEMPLATE = "Enter {}"
x = int(input(TEMPLATE.format('x: ')))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

a = (x/(x+11.3)+y/(z-11.3))
print("Result is: ", a)
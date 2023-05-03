# Introduction to programming, Lab № 4
# Roiaka Oleksii IKM-221a

print('Introduction to programming, Lab № 4')
print('Roiaka Oleksii IKM-221a')

TEMPLATE = "Enter {}"
N = int(input("Enter N: "))
for i in range(1, N+1):
    if str(i**2)[-len(str(i)):] == str(i):
        print(i)
num = int(input("Enter number: "))
rem = num % 2

if rem == 0:
    print("Even")
else:
    print("Odd")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is largest:", a)
elif b >= c:
    print("Second number is largest:", b)
else:
    print("Third number is largest:", c)

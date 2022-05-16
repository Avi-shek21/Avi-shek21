#Made_By_Abhishek
nu=("***CALCULATOR***")
print(nu.center(200))
print('1. Addition/Sum')
print('2. Product')
print('3. Subtract/Difference')
print('4. Division')
s = int(input("\nEnter operator number you want(1-4):\n"))
if s == 1:
	a = float(input("Enter first no."))
	b = float(input("Enter second no."))
	print("Sum is",a+b)
elif s == 2:
	a = float(input("Enter first no."))
	b = float(input("Enter second no."))
	print("Product is",a*b)
elif s ==3:
	a = float(input("Enter first no."))
	b = float(input("Enter second no."))
	print("Difference is",a-b)
elif s==4:
	a = float(input("Enter first no."))
	b = float(input("Enter second no."))
	print("Quotient is",a/b)
else:
	print("GALAT H MAM (1-4) CHOOSE KRO")
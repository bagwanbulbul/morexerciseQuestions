def factorial(n):
	fact = 1
	index = 1
	while index<=n:
		fact = index*fact
		index = index+1
	print fact
	return fact
n = int(raw_input("enter the number"))
factorial(n)


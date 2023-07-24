number1 = int(input("Enter first number: "))
operation = input("Enter operation: ")
number2 = int(input("Enter second number: "))
if operation =="+":
	print(number1+number2)
elif operation =="-":
	print(number1-number2)
elif operation =="*":
	print(number1*number2)
elif operation =="/":
	if(number2==0):
		print("Cannot divide 0")
	else:
		print(number1/number2)

else:
	print("Invalid operation")
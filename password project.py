counter = 5
default = "1234"
while True:
	password = input("Enter Password:")
	if default == password:
		print("Access Granted.")
		break
	else:
		print("Failed password, please try again. Tries left:")
		print(counter)
		counter-=1
		if counter == 0:
			print("Too many tries.")
			break
try:
	num=int(input("Enter the number: "))
	print(num**2)
except (KeyboardInterrupt):
	print("Only number is allowed.")
except (ValueError):
	print("Please check the input..")
print("BYE")

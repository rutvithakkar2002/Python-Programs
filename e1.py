num=int(input("Enter a number: "))
demo=int(input("Enter the denominator: "))
try:
	quo=num/demo
	print("Answer is: ",quo)
except ZeroDivisionError:
	print("can not divide a number by 0")

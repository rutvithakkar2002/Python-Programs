def divide(num,deno):
	try:
		quo=num/deno

	except ZeroDivisionError:
		print("can not divide a number by 0")
divide(10,0)


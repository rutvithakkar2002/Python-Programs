def divide(num,deno):
	return num/deno
try:
	ans=divide(10,0)
except ZeroDivisionError:
	print("Can not divide a number by 0")

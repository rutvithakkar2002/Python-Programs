str="Hello"
def msg():
	global var
	var="world"
	print("Inside function: "+ var)
msg()
print("str is: "+ str)
print("str is: "+ var)

var="Hello"
print("Before function: "+var)

def msg():
	global var
	var="world"
	print("Inside function "+ var)

msg()
print("outside function " + var)
var="python"
print("updated var "+ var)

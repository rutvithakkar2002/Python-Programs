no1=10
print("Global variable is "+ str(no1))

def fun(no2):	
	print("Inside function local variable is no2: "+str(no2))
	no3=30
	print("Inside fnction local variable is no3: "+str(no3))
fun(20)
print("outside function global vaariable is : "+str(no1))
#print("outside function global variable is: "+str(no3))

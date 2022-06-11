def increment(no):
	return((lambda no: no+10)(no))
no=int(input("enter no: "))
result=increment(no)
print(result)


no1=int(input("enter 1st number: "))
no2=int(input("enter 2nd number: "))
no3=int(input("enter 3rd number: "))
if((no1>no2)and(no1>no3)):
	print("no1 "+str(no1)+ "is maximum..")
elif((no2>no1)and(no2>no3)):
	print("no2 "+str(no2)+" is maximum..")
else:
	print("no3 "+str(no3)+"is maximum..")

sub1=float(input("enter marks of subject1: "))
sub2=float(input("enter marks of subject2: "))
sub3=float(input("enter marks of subject3: "))
sub4=float(input("enter marks of subject4: "))
sub5=float(input("enter marks of subject5: "))
total=0
total=sub1+sub2+sub3+sub4+sub5
print("total is "+str(total))
if((total<=100)and(total>=80)):
	print("Your gred is A")
elif((total>=70)and(total<80)):
	print("your gred is B")
elif((total>=60)and(total<70)):
	print("your gred is c")
elif((total>=50)and(total<40)):
	print("your gred is D")
elif((total<40)and(total>=0)):
	print("you are fail!")
else:
	print("Invalid marks!!!")

no=int(input("enter a number: "))
rev=0
while(no>0):
	rev=(rev*10)+i%10
	no=no//10
print("Reverse =",rev)

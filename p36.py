string=str(input("Enter a string: "))
count=0
for i in  string:
	count+=1
	for count in range(count,0,-1):
		print(string(count-1))

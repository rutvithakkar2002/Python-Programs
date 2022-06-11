def max_min(val):
	x=max(val)
	y=min(val)
	return(x,y)
list=[]

for i in range(5):
	list.append(int(input("Enter salary of employee[" +str(i+1) +"]: ")))

tup=tuple(list)
for index,val in enumerate(tup):
	print("Employee[ "+str(index+1)+"] is having salary: "+str(val))

(maximum,minimum)=max_min(tup)
print("maximum sal is "+ str(maximum))
print("minimum sal is "+str(minimum))

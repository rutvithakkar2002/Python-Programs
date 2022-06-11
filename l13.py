def add_2(x):
	x=x+2
	return x
num_list=[1,2,3,4,5,6,7]
new_list=list(map(add_2,num_list))
print(new_list)


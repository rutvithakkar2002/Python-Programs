import functools
def add(x,y):
	return x+y
num=[1,2,3,5]
print(functools.reduce(add,num))


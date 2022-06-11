#list=[[1,2,3],[4,5,6],[7,8,9]]
#print([val for x in list for val in x])
#spam="lottery"
#print(spam*2)
#double=lambda x:x*2
#sub=lambda x,y:x-y
#print(sub(double(5),9))
#import re
#pattern=r'[a-zA-Z]+\d+'
#obj=re.findall(pattern,'March 21,12 December,june 20,january 11')
#print(obj)
#fruits=['Apple','orange','Appricot','custerApple']
#new_list=list(map(lambda fruit:str.swapcase(fruit),fruits))
#print(new_list)
def func(x,y=200,z=100):
	print(x,y,z)
func(5,15,25)
func(35,z=55)
func(y=70,x=200)


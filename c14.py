def scale_x(x):
	return(x*10)
class no():
	def __init__(self,var):
		self.var=var
	def display(self):
		print("Number is: "+str(self.var))
	def modify(self):
		self.var=scale_x(self.var)
obj=no(10)
obj.display()
obj.modify()
obj.display()

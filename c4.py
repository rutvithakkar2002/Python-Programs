class demo:
	class_var=0
	def __init__(self,var):
		demo.class_var=demo.class_var+1
		self.var=var
		print("Object value is : ",var)
obj1=demo(5)
obj2=demo(10)


class demo():
	def __init__(self,var):
		self.var=var
	def display(self):
		print(self.var)
	def add_2(self):
		self.var=self.var+2
		self.display()
obj=demo(10)
obj.add_2()

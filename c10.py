class demo():
	def __init__(self,var):
		self.__var=var
	def __display(self):
		print("private method ",self.__var)
obj=demo(10)
obj._demo__display()


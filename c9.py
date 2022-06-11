class numbers:
	def __init__(self,var1,var2):
		self.var1=var1
		self.__var2=var2
	def display(self):
		print(self.var1)
		print(self.__var2)
obj=numbers(10,20)
obj.display()
print(obj.var1)
#print(obj.__var2)	private variable can not access outside the class.

class employee:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("Employee name is "+self.name)
e1=employee("Riya",22)
e2=employee("Rahul",24)
e1.display()
e2.display()

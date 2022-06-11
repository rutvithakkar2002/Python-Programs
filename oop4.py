class employee:
	name="Rahul"
	age=25
	def display_details(self,name,age):
		self.name="Divya"
		print("inside function: "+self.name)
		print("inside function: "+str(age))
e1=employee()
print(e1.name)
print(e1.age)
e1.display_details("Rohan",24)


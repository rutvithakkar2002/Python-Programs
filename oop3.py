class emp:
	name="Rahul"
	age=25
	def display_details(self):
		print("inside function: "+self.name)
		print("iside function: "+str(self.age))

e1=emp()
print(e1.name)
print(e1.age)
e1.display_details()

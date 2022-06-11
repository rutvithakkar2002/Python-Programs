class phone():
	def __init__(self,company):
		self.company=company
	def display(self):
		print("company of phone is: "+self.company)
samsung=phone("samsung")
samsung.display()
samsung.color="Black"  #new var
print("color of phone is: "+samsung.color)
samsung.color="Blue"  #updated newly vreated variable
print("Modified color of phone is: "+samsung.color)
del samsung.color   # deleting newly created variable

sam=phone("sam")
print(sam.color)


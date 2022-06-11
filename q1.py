class A:
	def display(self):
		print("Hello...")
class B:
	def display(self):
		print("word...")
class C(B):
	def display(self):
		print("It's Python")
obj=C()
obj.display()


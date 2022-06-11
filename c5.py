class Number:
	even=0
	def check(self,num):
		if(num%2==0):
			self.even=1
	def even_odd(self,num):
		self.check(num)
		if(self.even==1):
			print("Even")
		else:
			print("odd")
n=Number()	#Object creation
n.even_odd(5)

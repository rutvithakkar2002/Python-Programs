class Number:
	evens=[]
	odd=[]
	def __init__(self,num):
		self.num=num
		if(num%2==0):
			Number.evens.append(num)
		else:
			Number.odd.append(num)
n1=Number(31)
n2=Number(40)
print(Number.evens)
print(Number.odd)

del n1

class numbers:
	def __init__(self,list):
		self.list=list
	def __getitem__(self,index):
		return self.list[index]
	def __setitem__(self,index,val):
		self.list[index]=val
mylist=numbers([1,2,3,4,5,6,7])
print(mylist[5])
mylist[3]=10
print(mylist.list)


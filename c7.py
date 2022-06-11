class demo:
	def __init__(self,name,var):
		self.name=name
		self.var=var
	def __repr__(self):
		return repr(self.var)
	def __len__(self):
		return len(self.name)
	def __cmp__(self,obj):
		return self.var-obj.var
obj=demo("abcdef",10)
print("REPR",repr(obj))
print("Length",len(obj))
obj1=demo("ghijkl",1)
val=obj.__cmp__(obj1)
if(val==0):
	print("Same")
elif(val==-1):
	print("First one is larger")


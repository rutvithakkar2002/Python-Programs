def large(a,b):
	if(a>b):
		return a
	else:
		return b
sum=lambda x,y:x+y
diff=lambda x,y:x-y

print("Larger of 2 numbers: "+str(large(sum(-3,-2),diff(-1,2))))

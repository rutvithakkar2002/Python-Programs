l1=[1,3,5,7]
l2=[2,4,6,8]
print(l1)
l1[1]=[10,11,12]
l2[0]=l1
print(l2)
print(l1[1][:])
for i in l2:
	print(i,end="" )

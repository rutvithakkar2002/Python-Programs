s1="python"
#s2=s1
s2="programming"
s3="python"
print(id(s1))
print(id(s2))
print(id(s3))
if(id(s1)==id(s2)):
	print("same")
else:
	print("Differnt!")

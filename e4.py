try:
	file=open("file1.txt")
	str=f.readline()
	print(str)
except IOError:
	print("IOError")
else:
	print("No errors")


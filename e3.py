try:
	file=open("foo1.txt")
	str=f.readline()
	print(str)
except IOError:
	print("IOError!")
except ValueError:
	print("Value_error")
except:
	print("Unexpected error!")


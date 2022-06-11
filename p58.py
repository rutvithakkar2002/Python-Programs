def outer():
	var=100
	def inner():
		#var=200
		print("From inside function: "+str(var))
	inner()
	print("from outer function : "+str(var))
outer()

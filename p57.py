def outer():
	v_out=10
	def inner():
		v_in=20
		print("Outer var: "+str(v_out))
		print("Inner var: "+str(v_in))
	inner()
	print("outside function accessing out: "+str(v_out))
#	print("outside function aaccessing in: "+str(v_in))
outer()

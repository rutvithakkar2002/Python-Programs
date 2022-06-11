def remove(str):
	new_str=" "
	for i in str:
		if i in "aeiou":
			pass
		else:
			new_str+=i

	print(new_str)
remove("hello")
str="hello"
print(len(str))
print(str[len(str)-1])

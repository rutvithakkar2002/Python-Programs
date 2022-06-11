l1=[10,20,30,40,20,50,40]

def remove_duplicates(l1):
	unique=[]
	for element in l1:
		if element not in unique:
			unique.append(element)
	return unique

print(l1)
new_list=remove_duplicates(l1)
print(new_list)

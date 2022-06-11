def remove_dup(list):
	temp_list=[]
	for i in list:
		if i not in temp_list:
			temp_list.append(i)
	return temp_list

list=[1,2,3,1,2,4,5,6,6]
print(list)
new_list=remove_dup(list)
print(new_list)


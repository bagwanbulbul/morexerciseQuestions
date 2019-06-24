list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list = []
index = 0
while index<len(list1):
	index2 = 0
	while index2<len(list2):
		if list1[index] != list2[index2]:
		 new_list.append(list1[index])
		index2 = index2+1
	index = index+1
print new_list

list1 = [1, 342, 23, 75, 98]
list2 = [23, 75, 98, 12, 78, 10, 1]
index = 0
new_list = []
while index<len(list1):
	index2 = 0
	while index2<len(list2):
		if list1[index] == list2[index2]:
			new_list.append(list1[index])
		index2 = index2+1
	index = index+1
print new_list
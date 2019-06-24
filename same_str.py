string_list = ["rishab", "rishab", "abhishek", "rishab", "rishab", "divyashish", "divyashish"]
new_list = []
index = 0
while index<len(string_list):
	if  string_list[index] not in new_list:
		new_list.append(string_list[index])
	index = index+1
print new_list
words = "navgurukul is an alternative to higher education reducing the barriers of current formal education"
i = 0
new_list = []
while i<len(words):
	j = i
	space = ""
	while j<len(words):
		if words[j] == " ":
			break
		else:
			space = space+words[j]
		j = j+1
	new_list.append(space)
	i = j+1
print new_list
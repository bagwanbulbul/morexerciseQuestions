#loop runig ke liye 
index = 1
#1000 time tk hi loop chle 
while index<100:
	if index%21 == 0:
		print index,"navgurukul"
	elif index%7 == 0:
		print index,"gurukul"
	elif index%3 == 0:
		print index,"nav"
	index = index+1
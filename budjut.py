user_input = int(raw_input("number of students"))
user_input2 = int(raw_input("ek student ka kharcha"))
total_kharcha = user_input*user_input2
if total_kharcha<=50000:
	print "hum budget ke andar hain"
else: 
	print "hum budget ke bhar hain"
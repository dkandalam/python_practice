while 1 :
	x = input("enter the string")
	if x.lower() == 'bye' : 
		print "======###########========"
		break
	print "choose below oprations on the String"
	print "1:capitalize"
	print "2:lower"
	print "3:upper"
	opt = input()
	if opt == 1 :
		print x.capitalize()
	elif opt == 2 :
		print x.lower()
	elif opt == 3 :
		print x.upper()
	else :
		print "choose the right option"

	print "==========================="
 

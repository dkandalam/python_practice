print "this program to print max number from the entered digits"
max = 0
all = []
while(1):
	x = input(":")
	if x == ':':
		break
	all.append(x)
	if x > max :
		max = x
	

print "the entered numbers "+str(all)
print "the max from in the number "+str(max)

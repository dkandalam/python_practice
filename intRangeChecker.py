min,max = input("enter the min and max for a range")
x = input("enter a number between "+str(min)+","+str(max))
print "OK" if x >= min and x <= max else "number out of range"

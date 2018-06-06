array = eval(input('enter the number in bouble qoutes with comma'))
sum = 0.0
index = 0
while(index < len(array)) :
	sum+=array[index]
	index+=1

print "total",sum
print "average",sum/len(array)
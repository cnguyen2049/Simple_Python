""""
numbers = []
def loop(k,p):
	i =0
	while i<k:
		print "At the top i is %d" %i
		numbers.append(i)

		i = i+p
		print "Number now: ", numbers
		print "At the bottom i is %d" %i
loop(8,2)
print "The numbers: "

for num in numbers:
	print num
"""
numbers = []
for num in range(0,6):
	numbers.append(num)
	print num
print "Numbers []: ",numbers

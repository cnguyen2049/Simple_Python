# function 
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	# print statements with string substitution
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
# print statement
print "We can just give the function numbers directly:"
# function with integers as arguments
cheese_and_crackers(20,30)
# print statements
print "OR, we can use variables from out script:"
# variable with int value
amount_of_cheese = 10
# variable with int value
amount_of_crackers =50
# function with variables passed through it
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# print statement
print "We can even do math inside too:"
# function using math
cheese_and_crackers(10+20,5+6)
# print statement
print "And we can combine the two, varaible and math:"
# function with both variables and math
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)

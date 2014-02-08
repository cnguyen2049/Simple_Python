# print statement
print "Let's practice everything."
# print statement
print 'You\'d need to know \'bout espcapes with \\ that do \n newlines and \tabs.'
# multiple strings in poem
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanantion
\n\t\twhere there is none.
"""
# print statement
print "-------------"
# print statement
print poem 
# print statement
print "-------------"
# integer value in five
five= 10 -2 +3 -6
# print statement and string substitution 
print "This should be five: %s" % five
# function thats one argument 
def secret_formula(started):
	jelly_beans = started * 500
	jars= jelly_beans/1000
	crates =jars/100
	return jelly_beans,jars,crates
# new variable with int value
start_point = 10000
# value of variable from the function with the argument passed through
beans,jars,crates = secret_formula(start_point)
# print statement
print "With a starting point of: %d" % start_point
# pritn statement
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars,crates)
# divide value by 10
start_point = start_point / 10
# print statement
print "We can also do that his way:"
# print statement passing the function as string subed in 
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


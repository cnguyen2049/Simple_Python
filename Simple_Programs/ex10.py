print "I am 6'2\" tall." 
print 'I am 6\'2" tall.'
x = "\t"
y = '\\'
z = "\n"
tabby_cat= "%sI'm tabbed yee."%x
persian_cat ="I'm split%s on a line"%z
backslash_cat = "I'm %s a %s cat."%(y,y)

fat_cat ="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


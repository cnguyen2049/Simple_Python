# import from sys the argv feature
from sys import argv
# assign
script,filename = argv
# print statement
print "We're going to erase %r." % filename
# print statement
print "If you don't want that, hot CTRL-C (^C)."
# print statement
print "If you do want that hit, RETURn."
# ask for user command
raw_input("?")
# print statement
print "Opening the file..."
# open file 
target = open(filename, 'w')
# print statement
print "Truncating the file. Goodbye!"
# delete whats on file 
target.truncate()
# print statement
print "Now I'm going to ask you for three lines."
# ask for user input
line1 = raw_input("Line 1: ")
# user input
line2=  raw_input("Line 2: ")
# user input
line3=	raw_input("Line 3: ")
# print statement
print "I'm going to write these to the file."
# write in file
final_line = line1 + "\n" + line2 + "\n" +line3
target.write(final_line)
target.seek(0)
print temp.read()
# print statement
print "And finally, we close it."

# close file
target.close()

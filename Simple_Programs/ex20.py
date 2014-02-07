# import from sys "argv"
from sys import argv
# assign variable
script,input_file = argv
# function accepts f
def print_all(f):
	# read f
	print f.read()
# function one parameter
def rewind(f):
	# seek f
	f.seek(0)
# function accepts two parameters
def print_a_line(line_count,f):
	# print line count and the line in the file
	print line_count, f.readline()
# variable assigned to open the input file
current_file = open(input_file)
#print statement
print "First let's print the whole file:\n"
# print the entire file
print_all(current_file)
# print statement
print "Now let's rewind, kind of like tape"
# call rewind function on current file
rewind(current_file)
# print statement
print "Let's print three lines:"
# current line equals 1
current_line =1 # 1
# print the value of current file and the line it pertains to
print_a_line(current_line,current_file)
# current line equals previous value + 1
current_line +=1 # 2
# call function print file with current variables
print_a_line(current_line,current_file)
# add one more to current line
current_line += 1 #3
# call the function
print_a_line(current_line,current_file)


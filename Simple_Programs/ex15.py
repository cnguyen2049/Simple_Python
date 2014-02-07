# import feature of sys
from sys import argv 
# assign variables
script,filename =argv
# Open text
txt = open(filename)
# print statement
print "Here's your file %r:" %filename
# invoke read() on txt
print txt.read()
txt.close()
#print statement
print "Type the filename again:"
# assign user input to file
file_again = raw_input("> ")
#invoke open on file_again assign to txt again
txt_again = open(file_again)
# print txt again
print txt_again.read()
print txt_again.close()

from sys import argv

script,user_name,player_number = argv
prompt = 'Input please '
print "Hi %s, I'm the %s script."%(user_name,script)
print "I'd like yo ask  you a few questions about player %s."%player_number
print "Do you like me %s?" % user_name
likes= raw_input(prompt)

print "Where do you like %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer= raw_input(prompt)
print "What kind of player are you?"
data = raw_input(prompt)

print """
Alright so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. You are this %s type of player.
""" %(likes,lives,computer,data)


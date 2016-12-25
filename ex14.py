from sys import argv

script, Torrtoy = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (Torrtoy, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % Torrtoy
likes = raw_input(prompt)

print "Where do you live %s?" % Torrtoy
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about likeing me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer)

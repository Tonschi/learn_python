# -*- coding:utf-8 -*-

from sys import argv

script, userName = argv
prompt = '>'

print "Hi %s, I'm the %sscript." % (userName, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % userName
likes = raw_input (prompt)

print "Where do you live %s?" % userName
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input (prompt)

print """
Alright, do you said %r about liking me.
You life in %r. Not sure where that it.
And you have a %r computer. Nice!
""" % (likes, lives, computer)

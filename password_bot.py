#!/usr/bin/env python

from rivescript import RiveScript


rs = RiveScript(utf8=True)
rs.load_directory("./eg/brain")
rs.sort_replies()

print """Hello I'm Password Bot, I can assist you with strong passwords
------------------------------------------------------------------------------

"""

while True:
    msg = raw_input("You> ")
    if msg == '/quit':
        quit()
    reply = rs.reply("localuser", msg)
    print "Password Bot>", reply

# vim:expandtab
 
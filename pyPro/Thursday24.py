my_name = 'simcha levental'
my_age = 33 # not a lie
my_height = 74 # inches
my_weight = 200 # lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'
print "Let's talk about %s" %my_name
print "He's %s inches tall." % my_height
print "He's %s pounds heavy" % my_weight
print "Actualy he is not to heavy"
print "He's got %s eyes and %s hair" %(my_eyes, my_hair)
print "His teath are usualy %s depending on the coffee" % my_teeth
print "if I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# Ex. 6

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print  x
print y

print "I said: if %r" % x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w +e

#ex 7

print "Marry had a little lamb"
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#ex8

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this evening.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#ex 9

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApril\nMay\nJun\nJuly\nAug"
print "Here are the days: ", days
print "Here are the months: ", months

print """
sdcddcdc
scddscsd
scdscdc
scdcsd
"""

#ex10

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

print tabby_cat
print persian_cat
print backslash_cat

#ex11

print "How old are you",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "so, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)

# ex11

print "How old are you",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "so, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)

#Ex12

age = raw_input("How tall are you?", )
height = raw_input("How much do you weigh?")
weight = raw_input("How fat are you?")

print "so, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)

#ex13
from sys import argv

script, first, second, third = argv

print "Your  script is called:", script
print "Your  second:", second
print "Your third variable is:", third


#EX14

from sys import argv
script, user_name = argv
prompt = '> '

print "Hi %s, I am the %s script." % (user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "where do you like %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have "
computer = raw_input(prompt)

print """
Alright so you said %r about likeing me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice!
""" % (likes, lives, computer)

#EX15

from sys import argv

script,filename = argv

txt = open(filename)

print "Here's your file %r:" % filename

print txt.read()

print "i'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()




























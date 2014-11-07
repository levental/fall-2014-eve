## EX 20
# # imports the argv library
# from sys import argv
#
# # creates two variables
# script = argv[0]
# input_file = argv[1]
#
# def print_all(f):
#     print f.read()
#
# def rewind(f):
#     f.seek(0)
#
# def print_a_line(line_count, f):
#     print line_count, f.readline()
#
#
#
# current_file = open(input_file)
#
# print "First lets print the whole file:\n"
#
# print_all(current_file)
#
# print "Now lets rewind"
#
# rewind(current_file)
#
# print "let's print these three lines"
#
# current_line = 1
# print_a_line(current_line, current_file)
#
# current_line = current_line + 1
# print_a_line(current_line, current_file)
#
# current_line = current_line + 1
# print_a_line(current_line, current_file)

# def add(a, b):
#     print "ADDING %d + %d" %(a, b)
#     return a + b
# 
# def subt (a, b):
#     print "subtrackting %d + %d" %(a, b)
#     return a -
#
# age = add(30, 5)
#


import Ex25_lpthw.py
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
words['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
print words


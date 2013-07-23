from grading import *

pr = Group('Programming')
pr.headings = ['Objective']
pr.add(['Correct header information (author, description, time spent)'], 2)
pr.add(['Program builds and compiles'], 3)
pr.add(['Program demonstrates overall good design'], 3)
pr.add(['Program executes'], 3)
pr.add(['Program demonstrates good programming practices (internal comments, variables)'], 3)
pr.add(['Decimal places and calculations (including interest) are correct'], 3)
pr.add(['Menu structure functions correctly'], 3)

de = Group('Deductions')
de.headings = ['Objective']
de.add(['Sloppy code (indentation, variable names, etc)'], -3)

r = Rubric('Assignment 3','CSE100','Fall 2010')
r.add(pr)
r.add(de)

rep = Report(r,'students.csv')
rep.generate()

# we = Group('Written Exercises')
# we.headings = ['Chapter','Problem']
# we.add(['Chapter 1', 'Exercise 31'], 1)
# we.add(['Chapter 2', 'Exercise 14 B, C'], 2)
# we.add(['', 'Exercise 17 A-E'], 5)
# we.add(['', 'Exercise 25 C'], 1)
# we.add(['', 'Exercise 26 A'], 1)
# 
# pr = Group('Programming')
# pr.headings = ['Objective']
# pr.add(['Correct header information (author, description, time spent)'], 2)
# pr.add(['Program builds and compiles'], 3)
# pr.add(['Program prints name, birthday, hobbies, book, food'], 5)
# pr.add(['Program executes'], 3)
# pr.add(['Correct output which is neatly formatted'], 2)
# 
# de = Group('Deductions')
# de.headings = ['Objective']
# de.add(['Sloppy code (indentation, variable names, etc)'], -3)
# 
# r = Rubric('Assignment 1','CSE100', 'Fall 2010')
# r.add(we)
# r.add(pr)
# r.add(de)
# 
# rep = Report(r,'students.csv')
# rep.generate()